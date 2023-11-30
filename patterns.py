def print_square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def print_triangle_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

def print_inverted_triangle_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def print_pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def main():
    print("Square Pattern:")
    print_square_pattern(5)

    print("\nTriangle Pattern:")
    print_triangle_pattern(5)

    print("\nInverted Triangle Pattern:")
    print_inverted_triangle_pattern(5)

    print("\nPyramid Pattern:")
    print_pyramid_pattern(5)

if __name__ == "__main__":
    main()
