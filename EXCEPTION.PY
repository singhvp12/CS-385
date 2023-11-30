def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError as e:
        print(f"Error: {e}")
        result = None
    else:
        print(f"Result of {a} / {b}: {result}")
    finally:
        print("This block always executes.")

if __name__ == "__main__":
    # Example 1: Division by zero
    divide_numbers(5, 0)

    # Example 2: Correct division
    divide_numbers(10, 2)

    # Example 3: TypeError
    divide_numbers("10", 2)
