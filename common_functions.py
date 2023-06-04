import openai
import configparser
from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import yes_no_dialog

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

def cool_input(title, text):
    input_value = input_dialog(
        title=title,
        text=text
    ).run()

    if input_value is None:   # Check if the input is None
        input_value = ""      # Assign empty string if it is None
    
    return input_value


def checkbox(title,prompts):
	options = []

	for prompt in prompts:
		options.append((prompt, prompt))

    # Getting user inputs
	result = checkboxlist_dialog(
		title = title,
		text = "Select the desired options (use space to toggle)",
		values = options,
	).run()

	# Converting the user inputs to boolean values
	checked = []
	for prompt in prompts:
		if prompt in result:
			checked.append(True)
		else:
			checked.append(False)

	return checked

def yes_no(text = ""):
	return yes_no_dialog(
		title='Yes/No dialog example',
		text=text
		).run()