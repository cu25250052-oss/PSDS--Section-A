# Smallest Subarray with Sum Greater Than Target

def smallest_subarray(arr, target):
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink the window while sum is greater than target
        while current_sum > target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0

    return min_length


# Input array
arr = [2, 1, 5, 2, 3, 2]

# Target sum
target = 7

# Find smallest subarray
result = smallest_subarray(arr, target)

print("Array:", arr)
print("Target:", target)

if result == 0:
    print("No subarray found with sum greater than target.")
else:
    print("Smallest subarray length:", result)