# fibonaci number using function

# type 1
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ') 
        # default end is alway \n i.e, is new line
        a, b = b, a + b
    print()


fib(6)

# type 2 using append
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


print(fib2(6))

# fibonaci number using recursive for nth term 
def fib3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2)


print(fib3(6))


# fibonaci number using generator
# Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator function.
def fib4(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


print(list(fib4(6)))


# fibonaci with best space and time complexity
# findout the nth term of fibonacci number
def fib5(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib5(6))






