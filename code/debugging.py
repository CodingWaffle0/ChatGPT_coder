import openai
import sys

openai.api_key = "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"

def conversation_prep(pseudo = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me debugging code in {language}, walking me through setting up the debugging in VS code and suggesting different things that I should add to my code"},
		{"role": "user", "content":	f'here is the code that I need debugging:\n {pseudo}'}
	]
	return conversation

def get_response(conversation):
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

if __name__ == "__main__":
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		lan = sys.argv[2]

		conversation = conversation_prep(read_data_from_file(filename), lan)
		response = get_response(conversation);

		print(response['choices'][-1]['message']['content']);
		print('\n\n' + str(response['usage']))
	else:
		print("Please provide two file names as arguments.")