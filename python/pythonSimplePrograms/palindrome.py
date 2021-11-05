# cheack wether program is palindrome or not.


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrome("radar"))

# palindrome program without using list function


def palindrome2(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palindrome2(word[1:-1])


print(palindrome2("malylam"))

