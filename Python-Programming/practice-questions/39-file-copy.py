# Write a program that reads a text file and writes its output in another text file. The output
# should contain
# a. Number of letters
# b. Number of digits, and
# c. Number of other characters

def analyze_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()

        num_letters = 0
        num_digits = 0
        num_others = 0

        for char in content:
            if char.isalpha():
                num_letters += 1
            elif char.isdigit():
                num_digits += 1
            else:
                num_others += 1

        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Number of letters: {num_letters}\n")
            output_file.write(f"Number of digits: {num_digits}\n")
            output_file.write(f"Number of other characters: {num_others}\n")

        print(f"Analysis complete. Results written to {output_file_path}")

    except FileNotFoundError:
        print("The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = 'input.txt'
output_file_path = 'output.txt'

analyze_file(input_file_path, output_file_path)
