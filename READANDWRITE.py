# Writing to a file
def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to {file_name}\n")


# Reading from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content read from {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_name = "sample_file.txt"
    content_to_write = "Hello, this is a sample file content.\nPython is awesome!"

    # Writing to a file
    write_to_file(file_name, content_to_write)

    # Reading from a file
    read_from_file(file_name)
