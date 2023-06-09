from common_functions import *

def conversation_prep_first(code = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me debugging code in {language}, walking me through setting up the debugging in VS code and suggesting different things that I should add to my code"},
		{"role": "user", "content":	f'here is the code that I need debugging:\n {code}'}
	]
	return conversation

def setting_up_debbugging(filename, lan):
	conversation = conversation_prep_first(read_data_from_file(filename), lan)
	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

	conversation.append({
        'role': 'assistant',
        'content': response['choices'][-1]['message']['content']
    })

	return conversation

def isolating(conversation):
	conversation.append({
		"role": 'user',
		"content": f"How can I isolate the bug so that I know what to fix. The bug is {cool_input('Debugging', 'What is the bug')}"
	})

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

def fixing_bugs(conversation):
	while True:
		conversation.append({
			"role": 'user',
			"content": f"I have found that when doing, {cool_input('Debugging','When do you get problems')} I get {cool_input('Debugging', 'What is the problems')}. I think that it might be caused by {cool_input('Debugging', 'What might cause this')}"
		})

		response = get_response(conversation)

		print(response['choices'][-1]['message']['content'])
		print('\n\n' + str(response['usage']))

		if yes_no('Would you like to end'):
			break

def testing(conversation):
	conversation.append({
		"role": 'user',
		"content": "Can you make a test for this bug and tell me how to use it"
	})

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))


def main(filename, lan):
	conversation = setting_up_debbugging(filename, lan)

	if yes_no("Would you like help isolating the problem"):
		isolating(conversation)

	fixing_bugs(conversation)

	testing(conversation)
