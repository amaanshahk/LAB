def find_largest(numbers):
    if not numbers:
        return "List is empty"

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers_list = [5, 12, 3, 8, 7, 15, 1]
result = find_largest(numbers_list)
print(f"The largest number in the list is: {result}")
