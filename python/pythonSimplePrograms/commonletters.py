# Write a Python Program to Check Common Letters in Two Input Strings


def common_letters(str1, str2):
    """
    This function returns the common letters between two strings
    :param str1: First string
    :param str2: Second string
    :return: common letters
    """
    str1 = str1.lower()
    str2 = str2.lower()
    common_letters = ""
    for letter in str1:
        if letter in str2 and letter not in common_letters:
            common_letters += letter
    return common_letters

print(common_letters("Hello", "World"))
print(common_letters("nihal", "chandan"))
print(common_letters("Hello", "Hell"))

