import os

def get_output_file_name(base_name="wordlist", file_index=1):
    """
    Generates a file name based on the base name and file index (wordlist1.txt, wordlist2.txt, etc.).
    """
    return f"{base_name}{file_index}.txt"

def check_file_size(file_path):
    """
    Check the number of lines in the output file. Returns True if file has more than 1000 lines.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            line_count = sum(1 for _ in file)
            return line_count >= 1000
    return False
