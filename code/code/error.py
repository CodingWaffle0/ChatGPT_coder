from common_functions import *
import sys

def conversation_prep(code = "", error = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are an assistant who's job it is to help me find the error and fix it in this code in {language}."},
		{"role": "user", "content":	f'here is the code that I need help fixing the eroor:\n {code}, the error that having is {error}'}
	]
	return conversation

def suggestion():
	conversation = conversation_prep(read_data_from_file(filename), input("what is the error message: "), lan)
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
		if input('do you want to talk? (nothing means yes): ') != '':
			break

		conversation.append({
			"role": 'user',
			"content": input('')
		})

		response = get_response(conversation)

		print(response['choices'][-1]['message']['content'])
		print('\n\n' + str(response['usage']))

		conversation.append({
    	    'role': 'assistant',
    	    'content': response['choices'][-1]['message']['content']
    	})

if __name__ == "__main__":
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		lan = sys.argv[2]

		conversation = suggestion()

		talking(conversation)

	else:
		print("Please provide two file names as arguments.")