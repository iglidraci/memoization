"""
given an array of words return an array with all combinations that
we can construct a given target by
concatenating words from the array

Input -> 'python', ['py', 'thon', 'pyth', 'on', 'p', 'ython', 'boar']
Output -> [['py','thon'], ['pyth', 'on'], ['p', 'ython']]
"""

from typing import List


def all_construct(target:str, words:List[str])->int:
    """
    brute force approach
    we make this one work first then we use a hash map
    """
    all_combos = []
    if len(target) == 0:
        # the base case where we stop the recursion
        return [[]]
    for word in words:
        if target.startswith(word):
            temp_combo = all_construct(target.replace(word, ''), words)
            combo = map(lambda x:[word, *x], temp_combo)
            # don't want to append the array, want to spread the elements in it
            all_combos.append(*combo)
    return all_combos


def all_construct_memo(target:str, words:List[str], memo={'':[[]]})->int:

    if target in memo:
        return memo[target]

    all_combos = []

    for word in words:
        if target.startswith(word):
            temp_combo = all_construct_memo(target.replace(word, ''), words, memo)
            combo = map(lambda x:[word, *x], temp_combo)
            # don't want to append the array, want to spread the elements in it
            all_combos.append(*combo)
    memo[target] = all_combos
    return all_combos


target_word = 'python'
all_words = ['py', 'thon', 'pyth', 'on', 'p', 'ython', 'boar']


print(all_construct_memo(target_word, all_words))