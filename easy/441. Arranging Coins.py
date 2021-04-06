# Tag: math, Binary Search
'''
Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

SOL: simple math
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n+0.25)**0.5-0.5)