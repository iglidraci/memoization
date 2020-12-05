def fib(n:int, memo={0:1, 1:1})->int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

res = fib(100)
print(f'result is {res}')