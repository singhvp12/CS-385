# Example 1: Lambda function
square = lambda x: x ** 2
cube = lambda x: x ** 3

print("Example 1: Lambda function")
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print()

# Example 2: Map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
cubed_numbers = list(map(lambda x: x ** 3, numbers))

print("Example 2: Map function")
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Cubed numbers:", cubed_numbers)
print()

# Example 3: Filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Example 3: Filter function")
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
