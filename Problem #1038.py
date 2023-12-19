"""
Daily Coding Problem #1038

Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

input_str = input("Please enter your sentence: ")
wordlist = input_str.split(' ')

print("Given WordList: ", wordlist)

def reverse(lst):
    reverse_list = lst[::-1]
    return reverse_list

rev_wordlist = reverse(wordlist)
print("Reversed WordList: ", rev_wordlist)