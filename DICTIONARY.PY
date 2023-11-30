def dictionary_methods(my_dict):
    # Method 1: Accessing elements by key
    print("Method 1: Accessing elements by key")
    key = 'name'
    value = my_dict[key]
    print(f"The value for key '{key}': {value}\n")

    # Method 2: Adding a new key-value pair
    print("Method 2: Adding a new key-value pair")
    new_key = 'age'
    new_value = 25
    my_dict[new_key] = new_value
    print(f"Updated dictionary: {my_dict}\n")

    # Method 3: Removing a key-value pair using pop
    print("Method 3: Removing a key-value pair using pop")
    removed_value = my_dict.pop('age')
    print(f"Removed key-value pair: {removed_value}")
    print(f"Updated dictionary: {my_dict}\n")

    # Method 4: Getting a value with a default
    print("Method 4: Getting a value with a default")
    default_value = my_dict.get('country', 'Not available')
    print(f"Value for key 'country': {default_value}\n")

    # Method 5: Iterating through keys
    print("Method 5: Iterating through keys")
    for key in my_dict.keys():
        print(key, end=" ")
    print("\n")

    # Method 6: Iterating through values
    print("Method 6: Iterating through values")
    for value in my_dict.values():
        print(value, end=" ")
    print("\n")

    # Method 7: Iterating through key-value pairs
    print("Method 7: Iterating through key-value pairs")
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    print("\n")

    # Method 8: Clearing the dictionary
    print("Method 8: Clearing the dictionary")
    my_dict.clear()
    print(f"Cleared dictionary: {my_dict}\n")


if __name__ == "__main__":
    my_dict = {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}
    print(f"Original Dictionary: {my_dict}\n")

    dictionary_methods(my_dict)
