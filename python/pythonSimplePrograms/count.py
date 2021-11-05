# Write a Python Program to Count the Number of Digits in a Number?


def countDigits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


print(countDigits(12323))

# Write a Python Program to Count the Number of Digits in a Number using Recursion?


def countDigitsRecursion(n):
    if n == 0:
        return 0
    else:
        return 1 + countDigitsRecursion(n // 10)


print(countDigitsRecursion(12323))

# Write a Python Program to Count the Number using len function?


def countDigitsCount(n):
    return len(str(n))


print(countDigitsCount(12323))
