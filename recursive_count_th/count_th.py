"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    # Base case is when length is less than the
    #  characters we're looking for.
    if len(word) < 2:
        return 0

    # Cycle it over and over until it gets paired down
    #  to base case in order to pop out.
    if word[:2] == "th":
        return 1 + count_th(word[2:])

    # Chop off first character and keep cycling through
    return count_th(word[1:])
