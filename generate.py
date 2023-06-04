from common_functions import *


def conversation_prep(pseudo = "", language = ""):
	conversation = [
		{"role": "system", "content": f"You are a program takikng pseudo code into real {language} code. " + read_data_from_file("/home/willg/Coding/ChatGPT_coder/guidlines.txt")},
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

def main(input_filename, output_filename, lan):
	conversation = conversation_prep(read_data_from_file(input_filename), lan)
	response = get_response(conversation);

	print(response['usage'])

	write_data_to_file(output_filename, response['choices'][-1]['message']['content'])
