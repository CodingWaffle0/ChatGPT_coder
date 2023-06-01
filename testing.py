import sys

def read_data_from_file(input_file):
	try:
		with open(input_file, 'r') as f_in:
			data = f_in.read()
		return data
	except FileNotFoundError:
		print("Input file not found.")

def write_data_to_file(output_file, data):
	try:
		with open(output_file, 'w') as f_out:
			f_out.write(data)
		print("Data has been written to", output_file)
	except FileNotFoundError:
		print("Output file not found.")

if __name__ == "__main__":
	if len(sys.argv) == 3:
		input_filename = sys.argv[1]
		output_filename = sys.argv[2]
		print(read_data_from_file(input_filename))
		write_data_to_file(output_filename, "I think that this is going to work")
	else:
		print("Please provide two file names as arguments.")
