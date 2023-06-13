"""
Count Words in a String - Counts the number of individual words in a string.

https://github.com/karan/Projects
"""

string = input("Enter string to count words: ").lower()

#print(len(string.split())) <- Simple solution

# Solution where numbers are not words

from string import ascii_lowercase

def count_words(string: str) -> int:
    count = 0
    sub = ""
    for char in string:
        if char in ascii_lowercase:
            sub += char
        else:
            if sub == "":
                continue
            sub = ""
            count += 1
    if len(sub) > 0:
        count += 1
    return count

print(count_words(string))