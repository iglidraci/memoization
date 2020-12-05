"""
given an array of words return a bool if we can construct a given target by
concatenating words from the array
"""

from typing import List


def can_construct(target: str, words: List[str])->bool:
    """brute force approach"""
    if len(target) == 0:
        return True
    for word in words:
        if target.startswith(word):
            if can_construct(target.replace(word, ''), words):
                return True
    return False


def can_construct_memo(target: str, words: List[str], memo={'': True})->bool:
    """
    memoization technique
    """
    if target in memo:
        return memo[target]
    for word in words:
        if target.startswith(word):
            memo[target] = can_construct_memo(target.replace(word, ''), words, memo)
            if memo[target]:
                return True
    return False


print(can_construct_memo('skateboard', ['bo', 'd', 'ate', 't', 'ska', 'sk', 'boar']))