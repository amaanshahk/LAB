def is_perfect_number(num):
    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num


def generate_perfect_numbers(n):
    perfect_numbers = []
    num = 6  # The first perfect number is 6

    while len(perfect_numbers) < n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1

    return perfect_numbers

n = int(input("Enter the value of n: "))
result = generate_perfect_numbers(n)
print(f"The first {n} perfect numbers are: {result}")