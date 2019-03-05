#!/usr/local/bin/python3
bottles_to_count = 99

for bottle in range(bottles_to_count, 0, -1):
    if bottle > 2:
        print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer,\ntake one down, pass it around, {bottle-1} bottles of beer on the wall.\n")
    elif bottle == 2:
        print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer,\ntake one down, pass it around, {bottle-1} bottle of beer on the wall.\n")
    else:
        print(f"{bottle} bottle of beer on the wall, {bottle} bottle of beer,\ntake one down, pass it around, {bottle-1} bottle of beer on the wall.")
