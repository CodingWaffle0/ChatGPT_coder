import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_response(conversation):
	openai.api_key = config.get('API', 'key')
	return openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=conversation
	)

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