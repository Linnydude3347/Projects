"""
Pig Latin - Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).

https://github.com/karan/Projects
"""

string = input("Enter word to be translated to Pig Latin: ")
print(f"{string[1:]}-{string[0]}ay")