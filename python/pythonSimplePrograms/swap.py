# swap numbers using temporary variable


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(swap(a,b))

# swap numbers without using temporary variable


def swap2(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(swap2(a,b))


# swap numbers with 