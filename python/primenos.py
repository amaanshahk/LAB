def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_list(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

try:
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers_list = list(map(int, input_numbers.split()))

    prime_numbers = find_primes_in_list(numbers_list)

    if prime_numbers:
        print(f"The prime numbers in the list are: {prime_numbers}")
    else:
        print("There are no prime numbers in the list.")

except ValueError:
    print("Error: Please enter valid numbers.")
except KeyboardInterrupt:
    print("\nOperation aborted by the user.")
