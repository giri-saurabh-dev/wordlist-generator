import os
from wordlist_generator import generate_combinations
from utils import get_output_file_name, check_file_size

def main():
    # Get user input
    string = input("Enter the string (letters only, uppercase/lowercase): ")
    digits = input("Enter the digits (0-9): ")
    symbols = input("Enter the symbols (e.g., !@#$%): ")

    # Initializing file index
    file_index = 1
    output_file = get_output_file_name(file_index)

    while True:
        # Generate combinations
        combinations = generate_combinations(string, digits, symbols)

        # Check if the file exists and if it needs to be switched
        if check_file_size(output_file):
            file_index += 1
            output_file = get_output_file_name(file_index)
        
        # Write to output file
        with open(output_file, "a") as file:
            for word in combinations:
                file.write(word + "\n")

        print(f"Generated {len(combinations)} combinations in {output_file}.")
        
        # Ask the user if they want to continue generating
        user_input = input("Do you want to continue generating more words (y/n)? ")
        if user_input.lower() != 'y':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
