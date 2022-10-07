"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for currentItem in items:
        currentItem = str(currentItem)

        if currentItem in frequencies:
            frequencies[currentItem] += 1
        else:
            frequencies[currentItem] = 1

    return frequencies