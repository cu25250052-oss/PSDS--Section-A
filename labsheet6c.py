# Tower of Hanoi in Python

def tower_of_hanoi(n, source, auxiliary, destination):
    # Base condition
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main program
print("===== TOWER OF HANOI =====")

n = int(input("Enter the number of disks: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print(f"\nSteps to solve Tower of Hanoi for {n} disks:\n")

    tower_of_hanoi(n, "A", "B", "C")

    # Total number of moves
    total_moves = (2 ** n) - 1

    print(f"\nTotal number of moves: {total_moves}")