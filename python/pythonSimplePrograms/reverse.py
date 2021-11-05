# python program to reverse the number and string
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


def reverse_string(s):
    return s[::-1]

n = int(input("Enter the number: "))
print("The reverse of the number is: ", reverse(n))
s = input("Enter the string: ")
print("The reverse of the string is: ", reverse_string(s))



# python program to reverse the number and string using recursion
def reverse(n):
    if n == 0:
        return 0
    else:
        return n % 10 + reverse(n // 10)
    
def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])


n = int(input("Enter the number: "))
print("The reverse of the number is: ", reverse(n))
s = input("Enter the string: ")
print("The reverse of the string is: ", reverse_string(s))


