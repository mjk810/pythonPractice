import string


def str_range(start_value, end_value, step_value=1):
	'''
	Create a string iterator like the built in Python 'range' function

	Parameters
	----------
	start_value: string
		Value to start the iteration

	end_value: string
		Value to end the iteration (inclusive)
	step_value: int
		Optional step size parameter

	Returns
	-------
	generator
		characters between the start and end value
	'''
	alphabet = string.ascii_lowercase
	start_index = alphabet.index(start_value.lower())
	end_index = alphabet.index(end_value.lower())
	counter = start_index
	if step_value>=1:	
		while counter<=end_index:
			yield alphabet[counter]
			counter+=step_value
	else:
		while counter>=end_index:
			yield alphabet[counter]
			counter+=step_value

for letter in str_range('j','p'):
	print(letter),
print('\n')
for letter in str_range('c','a',-2):
	print(letter),
