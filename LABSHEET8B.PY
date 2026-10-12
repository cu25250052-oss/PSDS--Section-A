# Lab Sheet 8 - Question 2
# Longest Substring Without Repeating Characters

def longest_unique_substring(s):
    char_set = set()

    left = 0
    max_length = 0

    for right in range(len(s)):

        # Remove characters until current character is unique
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character
        char_set.add(s[right])

        # Calculate current window length
        current_length = right - left + 1

        max_length = max(max_length, current_length)

    return max_length


# Input
s = input("Enter the string: ")

# Calculate and display result
answer = longest_unique_substring(s)

print("Length of longest substring:", answer)