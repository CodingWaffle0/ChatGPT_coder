from common_functions import *

def main():
	conversation = [
		{"role": "system", "content": f"You are an assistant that tells me reasources and how I might going about things I want to learn"},
		{"role": "user", "content": cool_input("Learning", "What do you want to learn")}
	]

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))