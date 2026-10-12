# ============================================================
# IMPLEMENT MIN HEAP, MAX HEAP, PRIORITY QUEUE AND HEAP SORT
# ============================================================


# ------------------------------------------------------------
# MIN HEAP
# ------------------------------------------------------------

class MinHeap:

    def __init__(self):
        self.heap = []

    # Insert an element
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Move element upward
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # Remove minimum element
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return minimum

    # Move element downward
    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]

                index = smallest
            else:
                break

    def display(self):
        print(self.heap)


# ------------------------------------------------------------
# MAX HEAP
# ------------------------------------------------------------

class MaxHeap:

    def __init__(self):
        self.heap = []

    # Insert an element
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Move element upward
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]

                index = parent
            else:
                break

    # Remove maximum element
    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return maximum

    # Move element downward
    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = \
                    self.heap[largest], self.heap[index]

                index = largest
            else:
                break

    def display(self):
        print(self.heap)


# ------------------------------------------------------------
# PRIORITY QUEUE USING MIN HEAP
# ------------------------------------------------------------

class PriorityQueue:

    def __init__(self):
        self.heap = MinHeap()

    # Add element
    def enqueue(self, value):
        self.heap.insert(value)

    # Remove highest priority element
    def dequeue(self):
        return self.heap.extract_min()

    # Display queue
    def display(self):
        self.heap.display()


# ------------------------------------------------------------
# HEAP SORT
# ------------------------------------------------------------

def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):

        # Move maximum to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify remaining elements
        heapify(arr, i, 0)


# ============================================================
# MAIN PROGRAM
# ============================================================

print("========== MIN HEAP ==========")

min_heap = MinHeap()

values = [40, 20, 10, 30, 50, 5]

for value in values:
    min_heap.insert(value)

print("Min Heap:")
min_heap.display()

print("Extracted Minimum:", min_heap.extract_min())

print("Min Heap after deletion:")
min_heap.display()


print("\n========== MAX HEAP ==========")

max_heap = MaxHeap()

for value in values:
    max_heap.insert(value)

print("Max Heap:")
max_heap.display()

print("Extracted Maximum:", max_heap.extract_max())

print("Max Heap after deletion:")
max_heap.display()


print("\n========== PRIORITY QUEUE ==========")

pq = PriorityQueue()

pq.enqueue(40)
pq.enqueue(10)
pq.enqueue(30)
pq.enqueue(20)
pq.enqueue(5)

print("Priority Queue:")
pq.display()

print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())

print("Priority Queue after deletion:")
pq.display()


print("\n========== HEAP SORT ==========")

arr = [40, 10, 30, 50, 20, 60, 5]

print("Original Array:")
print(arr)

heap_sort(arr)

print("Sorted Array:")
print(arr)