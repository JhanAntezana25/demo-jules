def add(a, b):
  """Returns the sum of a and b."""
  return a + b

def subtract(a, b):
  """Returns the difference of a and b."""
  return a - b

def multiply(a, b):
  """Returns the product of a and b."""
  return a * b

def divide(a, b):
  """Returns the division of a by b. Raises ValueError if b is zero."""
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

if __name__ == "__main__":
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num1 = float(num1_str)
            num2_str = input("Enter the second number: ")
            num2 = float(num2_str)
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
            continue

        operation = input("Enter an operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            continue

        print(f"The result is: {result}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
