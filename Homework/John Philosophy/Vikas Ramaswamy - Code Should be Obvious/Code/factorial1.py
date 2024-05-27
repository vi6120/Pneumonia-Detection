def factorial(n):
    # Set the initial value of result to 1
    result = 1
    # Use a for loop to iterate over the range 1 to n+1
    for i in range(1, n+1):
        # Multiply the current value of result by i
        result *= i
    # Return the final value of result
    return result
