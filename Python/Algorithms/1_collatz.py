"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to
reach one using the following process: If n is even, divide it by 2. If n is odd,
multiply it by 3 and add 1.

https://github.com/karan/Projects
"""

n = int(input("Enter number for Collatz Conjecture: "))

def collatz(number: int) -> int:
    steps = 0
    while number != 1:
        if number % 2 != 0:
            number = (number * 3) + 1
            steps += 1
        while number % 2 == 0:
            number = number // 2
            steps += 1
    return steps

print(collatz(n))