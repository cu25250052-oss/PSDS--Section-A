# 3 Sum Problem in Python
# Find all unique triplets whose sum is equal to the target

def three_sum(arr, target):
    arr.sort()
    result = []

    n = len(arr)

    for i in range(n - 2):

        # Skip duplicate values
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == target:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicate values
                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

    return result


# Main Program
print("===== 3 SUM PROBLEM =====")

# Taking input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
target = int(input("Enter target sum: "))

# Find triplets
triplets = three_sum(arr, target)

# Display result
if triplets:
    print("\nTriplets whose sum is", target, "are:")

    for triplet in triplets:
        print(triplet[0], "+", triplet[1], "+", triplet[2], "=", target)
else:
    print("\nNo triplet found.")