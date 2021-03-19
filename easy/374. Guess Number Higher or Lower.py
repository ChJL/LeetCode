# Tag: Binary search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while guess(n)!=0:
            mid = lo + (n-lo)//2
            if guess(mid) == -1:
                n = mid - 1
            else:
                lo = mid + 1
        return n