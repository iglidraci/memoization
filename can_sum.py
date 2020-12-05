from typing import List


def can_sum(target: int, numbers: List[int])->bool:
    """
    Big O Analysis
    O(n^m) time complexity where n=target and m=len(numbers)
    O(m) space complexity, m stack calls
    """
    if target==0:
        return True
    for number in numbers:
        if target-number>=0:
            if can_sum(target-number, numbers):
                return True
    return False

def can_sum_memo(target: int, numbers: List[int], memo= {0:True})->bool:
    """
    Big O Analysis
    O(n*m) time complexity where n=target and m=len(numbers)
    O(m) space complexity, m stack calls
    """
    if target in memo:
        return memo[target]
    for number in numbers:
        if target-number>=0:
            memo[target] = can_sum_memo(target-number, numbers, memo)
            if memo[target]:
                return True
    return False


print('Calling the function ...')
print(can_sum_memo(300, [7, 14]))
print('Finished')