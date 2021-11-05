# anagram program


def anagram(word1, word2):
    """
    Checks if two words are anagrams of each other.
    """
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
   
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(anagram(word1, word2))


# anagram without using sorted()


def anagram2(word1, word2):
    """
    Checks if two words are anagrams of each other.
    """
    if len(word1) != len(word2):
        return False
    else:
        count = {}
        for letter in word1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in word2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(anagram2(word1, word2))
