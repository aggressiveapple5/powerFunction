#Power base function

def power_base(base, exponent):
	count = 1
	number = base 
	if exponent == 0:
			number = 1
	while count < exponent:
		number *= base
		count += 1

	return number
	
	
#- - - - - - - - - - - Main Program - - - - - - - - - - - 
	
	
base = int(raw_input("What would you like the base to be? "))
exponent = int(raw_input("What would you like the exponenet to be? "))
print(power_base(base, exponent))