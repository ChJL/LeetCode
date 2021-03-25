'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
SOL: Naive approach
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if not (i+1) % 15:
                res.append("FizzBuzz")
            elif not (i+1)%3:
                res.append("Fizz")
            elif not (i+1)%5:
                res.append("Buzz")
            else:
                res.append(str(i+1))
        return res