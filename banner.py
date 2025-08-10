# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:04:05 2024.

@author: Archik
"""


def banner_text(text: str = "", screen_width: float = 72) -> None:
    """
    Get an output of the `string` in banner or decorative format.

    This function work similar to that of print but adds decorative
    stars at the ends of specified or default screen_width. The
    printed output is centre aligned to the specified screen_width
    (excluding the space left for decorative asteric boundary). If
    the input is `*` then a line of star equal to screen_width is created.

    'Args':
        text (string): For normal `string` text will be printed
        in decorative described banner form and centre aligned.
        If text is `*` then a line of `*` will be printed equal
        to specified screen_width.

        screen_width (int, optional): The maximum number of
        characters allowed in a line (counting space). Defaults to 72.
    --------------------------------------

    'Raises':
        TypeError: if there is any error
    --------------------------------------

    'Returns':
        None: Always


    """
    # screen_width = 90
    if len(text) > screen_width - 4:
        print("EEK!")
        print("THE TEXT IS TOO LONG TO FIT IN SPECIFIED WIDTH")
    elif text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life ...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When your'e feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And ... always look on the bright side of life ...")
banner_text("*")

result = banner_text("Nothing is returned", 50)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())
banner_text(23, 45)
