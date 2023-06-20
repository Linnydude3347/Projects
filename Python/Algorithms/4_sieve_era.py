"""
Sieve of Eratosthenes - The sieve of Eratosthenes is one of the most efficient
ways to find all of the smaller primes (below 10 million or so).

https://github.com/karan/Projects
"""

def sieve(number: int) -> set[int]:
    multiples = set() # Sets are faster for membership tests
    result = []
    for i in range(2, number + 1):
        if i not in multiples:
            result.append(i)
            for j in range(i * i, number + 1, i):
                multiples.add(j)
    return result

print(sieve(100))