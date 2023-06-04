# Import necessary modules
import learning, generate, error, debugging, advancement
from common_functions import checkbox, cool_input, yes_no
import os


def main():
    # generate a checkbox, if they want help learning
    if yes_no("Do you want to learn?"): # update with checkbox value
        learning.main()

    input_str, output_str = cool_input("Enter file name", "Input: "), cool_input("Enter file name", "Output: ")
    lan = cool_input("Enter coding Language", "")

    if not validate_file_exists(input_str):
        return 1

    if yes_no("Do you want to generate?"):
        generate.main(input_str, output_str, lan)

    bugs, errors = checkbox("whats wrong", ["Is there any errors?", "Is there any bugs"]) # update with checkbox values
  
    if errors:
        error.main(output_str, lan)

    if bugs:
        debugging.main(output_str, lan)

    advancement.main(output_str)

def validate_file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print(f"The file '{filename}' does not exist.")
        return False

main()
