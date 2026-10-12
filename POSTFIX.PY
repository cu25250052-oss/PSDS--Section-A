# LAB ASSIGNMENT 5
# Postfix Expression Evaluation

class IntegerStack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def evaluate_postfix(expression):

    stack = IntegerStack()

    tokens = expression.split()

    for token in tokens:

        # If token is a number
        if token.lstrip('-').isdigit():

            stack.push(int(token))

        # If token is an operator
        elif token in "+-*/":

            second = stack.pop()
            first = stack.pop()

            if first is None or second is None:
                print("Invalid expression!")
                return None

            if token == '+':
                result = first + second

            elif token == '-':
                result = first - second

            elif token == '*':
                result = first * second

            elif token == '/':
                if second == 0:
                    print("Division by zero is not allowed!")
                    return None

                result = first // second

            stack.push(result)

        else:
            print("Invalid token:", token)
            return None

    return stack.pop()


# ---------------- MAIN PROGRAM ----------------

print("================================")
print("    POSTFIX EXPRESSION EVALUATION")
print("================================")

expression = input("Enter postfix expression: ")

answer = evaluate_postfix(expression)

if answer is not None:
    print("Postfix Expression:", expression)
    print("Final Result:", answer)