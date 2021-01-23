# Tag: Math
'''
Count the number of prime numbers less than a non-negative number, n.

SOL: Sieve of Eratosthenes: 
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Huahua: https://www.youtube.com/watch?v=Kwo2jkHOyPY

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        rec = [1 for i in range(n)]
        rec[0] = 0
        rec[1] = 0
        num = int(pow(n,0.5))
        for i in range(2, num+1):
            if not rec[i]:
                continue
            for j in range(i*i, n, i):
                rec[j] = 0
        #print(rec)
        return sum(rec)
            