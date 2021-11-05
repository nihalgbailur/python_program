#  Write a Python Program to Check if a Number is an Armstrong Number?
#  An Armstrong Number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.


def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


armstrong(153)






