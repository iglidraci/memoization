"""
given an array of words return the exact number of ways that
we can construct a given target by
concatenating words from the array
"""

from typing import List


def count_construct(target:str, words:List[str])->int:
    if len(target) == 0:
        return 1
    count = 0
    for word in words:
        if target.startswith(word):
            temp_count = count_construct(target.replace(word, ''), words)
            count += temp_count
    return count


def count_construct_memo(target:str, words:List[str], memo={'':1})->int:
    """
    count all the ways using memoization
    """
    if target in memo:
        return memo[target]
    count = 0
    for word in words:
        if target.startswith(word):
            memo[target] = count_construct_memo(target.replace(word, ''),\
                words, memo)
            count += memo[target]
    return count


print(count_construct_memo('python', ['py', 'thon', 'pyth', 'on', 'p', 'ython', 'boar']))