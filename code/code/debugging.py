from common_functions import *
import sys

def conversation_prep_first(pseudo = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me debugging code in {language}, walking me through setting up the debugging in VS code and suggesting different things that I should add to my code"},
		{"role": "user", "content":	f'here is the code that I need debugging:\n {pseudo}'}
	]
	return conversation

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

def isolating(conversation):
	conversation.append({
		"role": 'user',
		"content": "How can I isolate the bug so that I know what to fix. The bug is "
	})

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

def fixing_bugs(conversation):
	while True:
		conversation.append({
			"role": 'user',
			"content": f"I have found that when doing, {input('when do you get problems: ')} I get {input('what art he problems: ')}. I think that it might be caused by {input('what might cause this: ')}"
		})

		response = get_response(conversation)

		print(response['choices'][-1]['message']['content'])
		print('\n\n' + str(response['usage']))

		if input('would you like to end (nothing to end): ') == '':
			break

def testing(conversation):
	conversation.append({
		"role": 'user',
		"content": "Can you make a test for this bug and tell me how to use it"
	})

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))


if __name__ == "__main__":
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		lan = sys.argv[2]

		conversation = setting_up_debbugging()

		if input("would you like help isolating the problem (nothing mean no)") != '':
			isolating(conversation)

		fixing_bugs(conversation)

		testing(conversation)

	else:
		print("Please provide two file names as arguments.")