def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are remaining in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements are remaining in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



input_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original List: {input_list}")

merge_sort(input_list)

print(f"Sorted List: {input_list}")
