class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def precedence(operator):

    if operator == '^':
        return 3

    elif operator == '*' or operator == '/':
        return 2

    elif operator == '+' or operator == '-':
        return 1

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


# Main program

print("INFIX TO POSTFIX CONVERSION")

expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Infix   :", expression)
print("Postfix :", result)