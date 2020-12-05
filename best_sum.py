from typing import List

# give me the shortest combination that sums up to the given target

def best_sum(target: int, numbers: List[int])->List[int]:
    """
    Big O Analysis
    O(n^m * m) time complexity where n=target and m=len(numbers)
    times m because we have the spreading of array inside the for loop
    O(m) space complexity, m stack space
    """
    result = None
    if target==0:
        return []
    if target < 0:
        return None
    for number in numbers:
        temp_result = best_sum(target-number, numbers)
        if temp_result is not None:
            current_result = [*temp_result, number]
            if result is None or (len(current_result) < len(result)):
                result = current_result
    return result

def best_sum_memo(target: int, numbers: List[int], memo= {0:[]})->List[int]:
    """
    Big O Analysis
    """
    result = None
    if target in memo:
        return memo[target]
    if target < 0:
        return None
    for number in numbers:
        temp_result = best_sum_memo(target-number, numbers, memo)
        if temp_result is not None:
            current_result = [*temp_result, number]
            if result is None or (len(current_result) < len(result)):
                result = current_result
    memo[target] = result
    return result


print('Calling the function ...')
print(best_sum_memo(100, [1, 2, 5, 24]))
print('Finished')