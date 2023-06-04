# Import necessary modules
import learning, generate, error, debugging, advancement
import os


def main():
    input_str, output_str = input("Enter input: "), input("Enter output: ")
    lan = input("Enter language: ")

    if not validate_file_exists(input_str) or not validate_file_exists(output_str):
        return 1

    # generate a checkbox, if they want help learning
    if True: # update with checkbox value
        learning.main()

    generate.main(input_str, output_str, lan)
  
    bugs, errors = True, True # update with checkbox values
  
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
