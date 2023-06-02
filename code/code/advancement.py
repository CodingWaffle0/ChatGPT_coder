from common_functions import *
import sys

def improve(code = ''):
	conversation = [
		{"role": "system", "content": f"You are an assistant that tells me what I should improve about my codem, giving me examples"},
		{"role": "user", "content": f"here is the code: {code}"}
	]

	response = get_response(conversation)

	print(response['choices'][-1]['message']['content'])
	print('\n\n' + str(response['usage']))

if __name__ == "__main__":
	if len(sys.argv) == 2:
		filename = sys.argv[1]

		conversation = improve(read_data_from_file(filename))

	else:
		print("Please provide two file names as arguments.")