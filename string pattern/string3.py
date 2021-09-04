# Reverse words in a given String in Python
## initializing the string
string = "I am software developer"
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
# ## joining the words and printing
print(" ".join(words))
