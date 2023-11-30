def string_operations(input_string):
    # Length of the string
    length = len(input_string)
    print(f"Length of the string: {length}")

    # Concatenation
    new_string = input_string + " Concatenated"
    print(f"Concatenated string: {new_string}")

    # String repetition
    repeated_string = input_string * 3
    print(f"String repetition: {repeated_string}")

    # String slicing
    substring = input_string[2:6]
    print(f"Sliced substring (index 2 to 5): {substring}")

    # String uppercase and lowercase
    uppercase_string = input_string.upper()
    lowercase_string = input_string.lower()
    print(f"Uppercase string: {uppercase_string}")
    print(f"Lowercase string: {lowercase_string}")

    # String replace
    replaced_string = input_string.replace('Python', 'Java')
    print(f"String replace: {replaced_string}")

    # String find
    substring_index = input_string.find('is')
    print(f"Index of 'is': {substring_index}")

    # String count
    substring_count = input_string.count('is')
    print(f"Count of 'is': {substring_count}")

    # String split
    words = input_string.split(' ')
    print(f"String split into words: {words}")

    # String strip
    stripped_string = "   leading and trailing spaces   "
    stripped_result = stripped_string.strip()
    print(f"Stripped result: '{stripped_result}'")


if __name__ == "__main__":
    input_string = "Python is a powerful programming language."
    print(f"Original String: {input_string}\n")

    string_operations(input_string)
