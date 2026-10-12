class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue: Add element at the rear
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue: Remove element from the front
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        data = self.front.data
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        return data

    # Display queue
    def display(self):
        current = self.front

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())
q.display()

print("Dequeued:", q.dequeue())
q.display()