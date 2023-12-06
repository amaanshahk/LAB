def find_square_root(number, epsilon=1e-6):
    if number < 0:
        return "Cannot compute the square root of a negative number"

    low, high = 0, max(1, number)
    guess = (low + high) / 2

    while abs(guess**2 - number) > epsilon:
        if guess**2 < number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2

    return guess

input_number = float(input("Enter a number to find its square root: "))
result = find_square_root(input_number)

print(f"The square root of {input_number} is approximately {result:.6f}")
