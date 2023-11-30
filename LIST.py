def print_list_methods(my_list):
    # Method 1: Using a simple loop
    print("Method 1: Using a simple loop")
    for item in my_list:
        print(item, end=" ")
    print("\n")

    # Method 2: Using list comprehension
    print("Method 2: Using list comprehension")
    print(" ".join([str(item) for item in my_list]))
    print()

    # Method 3: Using map and join
    print("Method 3: Using map and join")
    print(" ".join(map(str, my_list)))
    print()

    # Method 4: Using * unpacking
    print("Method 4: Using * unpacking")
    print(*my_list)
    print()

    # Method 5: Using the pprint module
    import pprint
    print("Method 5: Using the pprint module")
    pprint.pprint(my_list)
    print()

    # Method 6: Using the print function with sep parameter
    print("Method 6: Using the print function with sep parameter")
    print(*my_list, sep=" ")
    print()


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(f"Original List: {my_list}\n")

    print_list_methods(my_list)
