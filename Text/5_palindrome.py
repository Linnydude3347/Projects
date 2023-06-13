"""
Check if Palindrome - Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”

https://github.com/karan/Projects
"""

string = input("Enter string to check for valid palindrome: ")
print(string == string[::-1])