# Rearrange array to maximize adjacent sum difference

def maximize_adjacent_difference(arr):
    arr.sort()

    n = len(arr)
    
    # Store elements in a special order
    result = [0] * n
    
    left = 0
    right = n - 1
    index = 0

    # Take largest, smallest, largest, smallest...
    while left <= right:
        if index < n:
            result[index] = arr[right]
            right -= 1
            index += 1

        if left <= right and index < n:
            result[index] = arr[left]
            left += 1
            index += 1

    # Calculate sum of adjacent absolute differences
    total = 0

    for i in range(n - 1):
        total += abs(result[i] - result[i + 1])

    return result, total


# Built-in input
arr = [1, 2, 3, 4, 5]

result, maximum_sum = maximize_adjacent_difference(arr)

print("Original Array:", arr)
print("Rearranged Array:", result)
print("Maximum Adjacent Difference Sum:", maximum_sum)