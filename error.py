from common_functions import *

def conversation_prep(code = "", error = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me find the error and fix it in this code in {language}."},
		{"role": "user", "content":	f'here is the code that I need help fixing the eroor:\n {code}, the error that having is {error}'}
	]
	return conversation

def suggestion(filename, lan):
	conversation = conversation_prep(read_data_from_file(filename), cool_input("Error","What is the error message"), lan)
	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

	conversation.append({
        'role': 'assistant',
        'content': response['choices'][-1]['message']['content']
    })

	return conversation

def talking(conversation):
	while True:
		if yes_no("Do you want to talk?"):
			break

		conversation.append({
			"role": 'user',
			"content": cool_input("Error", "What do you want to say?")
		})

		response = get_response(conversation)

		print(response['choices'][-1]['message']['content'])
		print('\n\n' + str(response['usage']))

		conversation.append({
    	    'role': 'assistant',
    	    'content': response['choices'][-1]['message']['content']
    	})

def main(filename, lan):

	conversation = suggestion(filename, lan)

	talking(conversation)