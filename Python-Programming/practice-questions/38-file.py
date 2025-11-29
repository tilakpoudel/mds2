# Write a program that reads a text file and displays the following:
# a. Number of characters
# b. Number of vowels
# c. Number of consonants
# d. Number of words
# e. Number of lines

# Create a text file named 'sample.txt' with some content to test the program.
def create_sample_file():
    sample_content = """Hello World!
        This is a sample text file.
        It contains multiple lines, words, and characters.
        Feel free to modify it as needed."""
    
    with open('sample.txt', 'w') as file:
        file.write(sample_content)

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

        num_lines = len(content)
        num_words = 0
        num_characters = 0
        num_vowels = 0
        num_consonants = 0
        vowels = "aeiouAEIOU"

        for line in content:
            num_characters += len(line)
            words_in_line = line.split()
            num_words += len(words_in_line)

            for char in line:
                if char.isalpha():
                    if char in vowels:
                        num_vowels += 1
                    else:
                        num_consonants += 1

        print(f"Number of characters: {num_characters}")
        print(f"Number of vowels: {num_vowels}")
        print(f"Number of consonants: {num_consonants}")
        print(f"Number of words: {num_words}")
        print(f"Number of lines: {num_lines}")

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
create_sample_file()
file_path = 'sample.txt'

analyze_file(file_path)
