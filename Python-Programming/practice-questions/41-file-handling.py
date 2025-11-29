# Write a program to find sum and average of numbers stored in a file. Create a separate file to
# write output.

def calculate_sum_and_average(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().isdigit()]

        if not numbers:
            raise ValueError("No valid numbers found in the file.")

        total_sum = sum(numbers)
        average = total_sum / len(numbers)

        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Sum: {total_sum}\n")
            output_file.write(f"Average: {average}\n")

        print(f"Sum and average have been written to {output_file_path}")

    except FileNotFoundError:
        print("The input file was not found.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = 'numbers.txt'  # Make sure to have a file named 'numbers.txt with numbers in the same directory
output_file_path = 'output.txt'

calculate_sum_and_average(input_file_path, output_file_path)
