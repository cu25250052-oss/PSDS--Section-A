# Lab Sheet 8 - Question 1
# Maximum Sum of Contiguous Subarray of Size K

def max_subarray_sum(arr, k):
    n = len(arr)

    # Sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, n):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


# Input
n, k = map(int, input("Enter N and K: ").split())

arr = list(map(int, input("Enter array elements: ").split()))

# Calculate and display result
answer = max_subarray_sum(arr, k)

print("Maximum sum:", answer)