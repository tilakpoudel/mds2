# Write a program that reads the file containing texts and counts the number of whitespaces.

def count_whitespaces_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            whitespace_count = sum(1 for char in content if char.isspace())

        return whitespace_count
    except FileNotFoundError:
        print("The specified file was not found.")

        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return None
    
# Example usage
file_path = 'sample.txt'  # Make sure to have a file named 'sample.txt in the same directory
whitespace_count = count_whitespaces_in_file(file_path)

if whitespace_count is not None:
    print(f"Number of whitespaces in the file: {whitespace_count}")
