# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

def read_file():
    file_name = input("Enter the name of the file to read: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")

if __name__ == "__main__":
    read_file()