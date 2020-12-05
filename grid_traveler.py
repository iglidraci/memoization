"""
we got a 2D grid and a traveller starting from up left and reaching down right
he/she can only move down or right, not up, not diagonal

print how many different ways the traveler can reach the destination
"""


def grid_travaler(x, y, memo= {(1,1):1})->int:
    if x ==0 or y==0:
        return 0
    if (x,y) in memo:
        return memo[(x,y)]
    memo[(x,y)] = grid_travaler(x-1, y, memo) + grid_travaler(x, y-1, memo)
    return memo[(x,y)]

print('calling ...')
print(grid_travaler(18,18))
print('Tadaaa')

"""
***Big O Analisys***
Time complexity
O(mxn)
Space complexity
O(m+n)
"""