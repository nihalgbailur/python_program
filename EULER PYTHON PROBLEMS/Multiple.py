# Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

# TEST CASES
# multiplesOf3and5(49) should return 543.
# Waiting:multiplesOf3and5(1000) should return 233168.
# Waiting:multiplesOf3and5(8456) should return 16687353.
# Waiting:multiplesOf3and5(19564) should return 89301183.

def sum_of_multiples_of_3_and_5(number):
    total_sum = 0
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum

# Example usage:
parameter_value = int(input("value "))
result = sum_of_multiples_of_3_and_5(parameter_value)
print("The sum of multiples of 3 or 5 below", parameter_value, "is:", result)
