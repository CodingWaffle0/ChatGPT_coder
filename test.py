# Importing necessary module
from prompt_toolkit.shortcuts import checkboxlist_dialog

def checkbox(prompts):


    # Getting user inputs
	result = checkboxlist_dialog(
		title = "whats wrong",
		text = "Select the desired options (use space to toggle)",
		values = options,
	).run()

	# Converting the user inputs to boolean values
	checked = []
	for prompt in prompts:
		if prompt in result:
			checked.append(True)
		else:
			checked.append(False)

	return checked