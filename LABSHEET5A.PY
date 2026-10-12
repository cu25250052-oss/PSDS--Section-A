
# LAB ASSIGNMENT 5
# Q1: Infix to Postfix Conversion

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""

    for ch in expression:

        # Operand
        if ch.isalnum():
            postfix += ch

        # Opening bracket
        elif ch == '(':
            stack.push(ch)

        # Closing bracket
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()

            if not stack.is_empty():
                stack.pop()

        # Operator
        elif ch in "+-*/^":
            while (
                not stack.is_empty()
                and stack.peek() != '('
                and precedence(stack.peek()) >= precedence(ch)
            ):
                postfix += stack.pop()

            stack.push(ch)

    # Pop remaining operators
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


# ---------------- MAIN PROGRAM ----------------

print("===================================")
print("       INFIX TO POSTFIX")
print("===================================")

expression = input("Enter infix expression: ")

postfix = infix_to_postfix(expression)

print("\nInfix Expression  :", expression)
print("Postfix Expression:", postfix)

print("\nProgram executed successfully!")

