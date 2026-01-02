# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 19:45:49 2025.

@author: Archik
"""

import json
import os
import pandas as pd
from typing import List, Dict, Any, Optional
from groq import Groq
import difflib

# -------------------------------------------------
# 1️⃣ Load data from Excel → structured list of dicts
# -------------------------------------------------
def load_real_data(excel_path: str = r"C:\\Users\\hanum\\Downloads\\Swiggy_Menu_Sample.xlsx") -> List[Dict[str, Any]]:
    df = pd.read_excel(excel_path)

    # ----------------------------------------------------------------------
    # Normalise column names – adjust if your sheet uses slightly different names
    # ----------------------------------------------------------------------
    df = df.rename(columns={
        'Restaurant_name': 'resto_name',
        'address': 'resto_address',
        'cuisines': 'resto_cuisines',
        'total_ratings': 'resto_rating',
        'category_name': 'category',
        'item_Name': 'item_name',
        'item_price': 'item_price',
        'item_Image': 'item_image'
    })

    # Split the pipe‑separated cuisine list into a Python list
    df['resto_cuisines'] = df['resto_cuisines'].apply(
        lambda x: str(x).split('|') if pd.notna(x) else []
    )

    restaurants: List[Dict[str, Any]] = []

    # ----------------------------------------------------------------------
    # Build one dict per restaurant
    # ----------------------------------------------------------------------
    for _, resto_row in df.drop_duplicates('resto_name').iterrows():
        resto_df = df[df['resto_name'] == resto_row['resto_name']]

        resto = {
            'id': resto_row.get('Restaurant_id', 'unknown'),
            'name': resto_row['resto_name'],
            'address': f"{resto_row.get('streetAddress', '')}, {resto_row.get('addressLocality', '')}".strip(', '),
            'cuisines': resto_row['resto_cuisines'],
            'rating': resto_row.get('resto_rating', 0),
            'menu': []                     # <-- list of categories
        }

        # ------------------------------------------------------------------
        # Group by category (e.g., "Recommended", "Main Course")
        # ------------------------------------------------------------------
        for cat_name, cat_df in resto_df.groupby('category'):
            if pd.isna(cat_name):
                continue

            items = []
            for _, row in cat_df.iterrows():
                item_name = row.get('item_name')
                if pd.isna(item_name):
                    continue

                # ---- Simple veg / non‑veg heuristic ----
                lower = str(item_name).lower()
                non_veg_keywords = ['chicken', 'mutton', 'fish', 'egg', 'non veg', 'non-veg']
                is_veg = not any(k in lower for k in non_veg_keywords)

                item: Dict[str, Any] = {
                    'name': item_name,
                    'price': float(row.get('item_price', 0)),
                    'veg': is_veg
                }
                if pd.notna(row.get('item_image')):
                    item['image'] = row['item_image']
                items.append(item)

            if items:
                resto['menu'].append({
                    'category': str(cat_name),
                    'items': items
                })

        if resto['menu']:
            restaurants.append(resto)

    return restaurants


# -------------------------------------------------
# 2️⃣ Groq helper utilities
# -------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
USE_GROQ = client is not None


def _clean_groq_response(text: str) -> str:
    """Strip optional markdown fences and surrounding whitespace."""
    text = text.strip()
    if text.startswith("```"):
        # remove the first line (```json or ```)
        parts = text.split("\n", 1)
        if len(parts) == 2:
            text = parts[1]
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
    return text.strip()


def extract_filters(query: str) -> Dict[str, Any]:
    """
    Ask Groq to turn a free‑text query into a structured filter dict.
    Fallback to a very permissive dict if the API fails.
    """
    prompt = f"""
You are a smart food‑search assistant for Abohar restaurants.
User query: "{query}"

Extract the following fields **as valid JSON** (use null when unknown):
- restaurant: partial restaurant name (string or null)
- dish: dish keyword (string or null)
- max_price: maximum price in INR (number or null)
- veg_only: true / false / null
- category: menu category (string or null)

Only output the JSON, nothing else.
"""

    if not USE_GROQ:
        # -------------------------- Offline fallback -------------------------
        return {
            "restaurant": None,
            "dish": query.lower(),
            "max_price": None,
            "veg_only": None,
            "category": None,
        }

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=150,
        )
        raw = response.choices[0].message.content or ""
        cleaned = _clean_groq_response(raw)
        return json.loads(cleaned)
    except Exception as exc:
        print(f"[Groq] error → {exc!s}. Using permissive fallback.")
        return {
            "restaurant": None,
            "dish": query.lower(),
            "max_price": None,
            "veg_only": None,
            "category": None,
        }


# -------------------------------------------------
# 3️⃣ Search logic
# -------------------------------------------------
def _matches_substring(pattern: Optional[str], text: str) -> bool:
    """Case‑insensitive substring OR fuzzy match (ratio > 0.7)."""
    if not pattern:
        return True
    pattern = pattern.lower()
    text = text.lower()
    if pattern in text:
        return True
    # fuzzy fallback – only for short queries (<8 chars) to avoid false positives
    if len(pattern) <= 8:
        matches = difflib.get_close_matches(pattern, [text], n=1, cutoff=0.7)
        return bool(matches)
    return False


def search_menu(query: str, restaurants: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    filters = extract_filters(query)

    results = []
    for resto in restaurants:
        # ---- restaurant name filter ----
        if not _matches_substring(filters.get("restaurant"), resto["name"]):
            continue

        for cat in resto["menu"]:
            # ---- category filter ----
            if not _matches_substring(filters.get("category"), cat["category"]):
                continue

            for item in cat["items"]:
                # ---- dish keyword filter ----
                if not _matches_substring(filters.get("dish"), item["name"]):
                    continue

                # ---- veg / non‑veg filter ----
                veg_flag = filters.get("veg_only")
                if veg_flag is True and not item["veg"]:
                    continue
                if veg_flag is False and item["veg"]:
                    continue

                # ---- price filter ----
                max_price = filters.get("max_price")
                if max_price is not None and item["price"] > max_price:
                    continue

                results.append({
                    "restaurant": resto["name"],
                    "address": resto["address"],
                    "rating": resto["rating"],
                    "category": cat["category"],
                    "item": item,
                })
    return results


# -------------------------------------------------
# 4️⃣ Pretty printing
# -------------------------------------------------
def display_results(matches: List[Dict[str, Any]]) -> None:
    if not matches:
        print("\n❌ Nothing found! Try queries like 'shahi paneer', 'veg under 250', 'main course'")
        return

    print(f"\n🍲 {len(matches)} match{'es' if len(matches)!=1 else ''}:\n")
    for m in matches:
        item = m["item"]
        price = f"₹{item['price']:.0f}"
        veg_emoji = "🟢 Veg" if item["veg"] else "🔴 Non‑Veg"

        print(f"🍽️ {m['restaurant']}  ⭐ {m['rating']}")
        print(f"   📍 {m['address']}")
        print(f"   📂 {m['category']} → {item['name']:<35} {price:>10}  {veg_emoji}")
        print("   " + "─" * 60)


# -------------------------------------------------
# 5️⃣ Main REPL
# -------------------------------------------------
def main() -> None:
    # Load once – keep it in memory
    restaurants = load_real_data()

    print("\n🍴 Smart Food Finder (Swiggy data + Groq AI) 🍴")
    print("Examples:  'paneer',  'veg main course under 300',  'chilli'\n")

    while True:
        try:
            query = input("🔍 Craving? → ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Bye! 🍲")
            break

        if query.lower() in {"quit", "exit", "q"}:
            print("\n👋 Bye! 🍲")
            break
        if not query:
            continue

        matches = search_menu(query, restaurants)
        display_results(matches)


if __name__ == "__main__":
    main()
