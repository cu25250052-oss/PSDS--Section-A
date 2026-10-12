
# LAB ASSIGNMENT 5
# Q2: Postfix Expression Evaluation

class IntegerStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def evaluate_postfix(expression):

    stack = IntegerStack()

    # Split expression using spaces
    tokens = expression.split()

    for token in tokens:

        # If token is a number
        if token.lstrip('-').isdigit():
            stack.push(int(token))

        # If token is an operator
        elif token in "+-*/^":

            second = stack.pop()
            first = stack.pop()

            if first is None or second is None:
                print("Invalid postfix expression!")
                return None

            if token == '+':
                result = first + second

            elif token == '-':
                result = first - second

            elif token == '*':
                result = first * second

            elif token == '/':
                if second == 0:
                    print("Error: Division by zero!")
                    return None
                result = first // second

            elif token == '^':
                result = first ** second

            stack.push(result)

        else:
            print("Invalid token:", token)
            return None

    result = stack.pop()

    if not stack.is_empty():
        print("Invalid postfix expression!")
        return None

    return result


# ---------------- MAIN PROGRAM ----------------

print("===================================")
print("      POSTFIX EXPRESSION EVALUATOR")
print("===================================")

print("\nExample:")
print("2 3 * 5 4 * +")

expression = input("\nEnter postfix expression: ")

answer = evaluate_postfix(expression)

if answer is not None:
    print("\nPostfix Expression:", expression)
    print("Final Result:", answer)

print("\nProgram executed successfully!")

