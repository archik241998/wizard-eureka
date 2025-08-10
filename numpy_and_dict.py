# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:20:21 2024.

@author: Archik
"""
import numpy as np
a = np.random.normal(25.0, 5.0, 10)
print(a)


captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])
print(captains.get("Enterprise"))
print(captains.get("NX-01"))

for ship in captains:
    print(ship + ": " + captains[ship])
