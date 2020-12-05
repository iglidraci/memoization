from typing import List

# just give me a combination that sums to the given target

def how_sum(target: int, numbers: List[int])->List[int]:
    """
    Big O Analysis
    O(n^m * m) time complexity where n=target and m=len(numbers)
    times m because we have the spreading of array inside the for loop
    O(m) space complexity, m stack space
    """
    if target==0:
        return []
    if target < 0:
        return None
    for number in numbers:
        result = how_sum(target-number, numbers)
        if result is not None:
            return [*result, number]
    return None

def how_sum_memo(target: int, numbers: List[int], memo= {0:[]})->List[int]:
    """
    Big O Analysis
    O(n*m * m)=O(n*m^2) time complexity where n=target and m=len(numbers)
    O(m*m)=O(m^2) space complexity, m stack calls and for each stack call we might
    have a dictionary of m element array as value
    """
    if target in memo:
        return memo[target]
    if target < 0:
        return None
    for number in numbers:
        memo[target] = how_sum_memo(target-number, numbers, memo)

        if memo[target] is not None:
            return [*memo[target], number]
    return None


print('Calling the function ...')
print(how_sum_memo(300, [1]))
print('Finished')