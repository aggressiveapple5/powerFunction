def power_base(base, exponent):
	
	 
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
		
	
	
	return base * power_base(base , exponent - 1)
	
	
def int_input(prompt):
	'''Ask the user for an int and let them try again.'''
	
	answer = raw_input(prompt)
	#Terminating Case
	try:
		answer = int(answer)
		return answer
	except ValueError:
		return(int_input("That was not an interger. Try again."))
		
		
def float_input(prompt):
	'''Asks the user for a float and lets them try again.'''
	
	answer = raw_input(prompt)
	
	try: 
		answer = float(answer)
		return answer
	except ValueError:
		return(int_input("That was not an interger. Try again."))