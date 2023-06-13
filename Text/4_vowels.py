"""
Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.

https://github.com/karan/Projects
"""

string = input("Enter string to count vowels: ").lower()
vowels = "aeiou"
result = sum(c in vowels for c in string)
print(result)