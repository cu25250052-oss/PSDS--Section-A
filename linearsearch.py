arr = [10, 20, 30, 40, 50]

search = int(input("Enter element to search: "))

found = False

for i in range(5):
    if arr[i] == search:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")