# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

def load_file_content(file_name):
    """Returns the content of a file or an error message."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"File content:\n{content}"
    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist. Please check the file name and try again."

def read_file():
    """Handles user interaction."""
    file_name = input("Enter the name of the file to read: ")
    message = load_file_content(file_name)
    print(message)

if __name__ == "__main__":
    read_file()
