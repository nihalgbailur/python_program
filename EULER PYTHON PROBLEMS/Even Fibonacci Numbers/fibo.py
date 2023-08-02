def even_fibonacci_sum(n):
    fib_seq = [1, 2]
    even_sum = 2  # The sum starts at 2 since 2 is the first even term

    while True:
        next_term = fib_seq[-1] + fib_seq[-2]
        if next_term > n:
            break

        if next_term % 2 == 0:
            even_sum += next_term

        fib_seq.append(next_term)

    return even_sum

# Example usage:
n = 34  # Change this value to the desired limit
result = even_fibonacci_sum(n)
print("The sum of even-valued Fibonacci terms not exceeding", n, "is:", result)
