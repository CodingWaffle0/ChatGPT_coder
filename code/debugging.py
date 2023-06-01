import openai
import sys

openai.api_key = "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"

def conversation_prep_first(pseudo = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me debugging code in {language}, walking me through setting up the debugging in VS code and suggesting different things that I should add to my code"},
		{"role": "user", "content":	f'here is the code that I need debugging:\n {pseudo}'}
	]
	return conversation

def conversation_prep_second(converstation):
	converstation.append({
		"role": 'user',
		"content": f"I have found that when doing, {input('when do you get problems: ')} I get {input('what art he problems: ')}. I think that it might be caused by {input('what might cause this: ')}"
	})

	return converstation

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

def setting_up_debbugging():
	conversation = conversation_prep_first(read_data_from_file(filename), lan)
	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

	conversation.append({
        'role': 'assistant',
        'content': response['choices'][-1]['message']['content']
    })

	return conversation

def fixing_bugs(conversation):
	while True:
		conversation = conversation_prep_second(conversation)

		response = get_response(conversation)

		print(response['choices'][-1]['message']['content'])
		print('\n\n' + str(response['usage']))

		if input('would you like to end (nothing to end): ') == '':
			break


if __name__ == "__main__":
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		lan = sys.argv[2]

		conversation = setting_up_debbugging()

		fixing_bugs(conversation)

	else:
		print("Please provide two file names as arguments.")