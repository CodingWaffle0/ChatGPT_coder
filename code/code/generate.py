from common_functions import *
import sys



def conversation_prep(pseudo = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are a program takikng pseudo code into real {language} code. " + read_data_from_file("guidlines.txt")},
		{"role": "user", "content":	'turn this into unity 2d code: fn main{\n	print!("I like men");\n}'},
		{"role": "assistant", "content": """using UnityEngine;

public class PrintText : MonoBehaviour
{
    void Start()
    {
        Debug.Log("I like men");
    }
}
"""},
		{"role": "user", "content": f"turn this into {language} code: {pseudo}"}
	]

	return conversation

if __name__ == "__main__":
	if len(sys.argv) == 4:
		input_filename = sys.argv[1]
		output_filename = sys.argv[2]
		lan = sys.argv[3]

		conversation = conversation_prep(read_data_from_file(input_filename), lan)
		response = get_response(conversation);

		print(response['usage'])

		write_data_to_file(output_filename, response['choices'][-1]['message']['content'])


	else:
		print("Please provide two file names as arguments.")