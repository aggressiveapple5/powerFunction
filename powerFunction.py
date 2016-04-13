# Power base function
# TODO INSERT DOC STRING
# def power_base(base, exponent):
# 	count = 1
# 	number = base 
# 	if exponent == 0:
# 			number = 1
# 	while count < exponent:
# 		number *= base
# 		count += 1
# 
# 	return number
# 	

def power_base(base, exponent):
	
	 
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	
	return base * power_base(base , exponent - 1)
	
	
#- - - - - - - - - - - Main Program - - - - - - - - - - - 
	
	
base = int(raw_input("What would you like the base to be? "))
exponent = int(raw_input("What would you like the exponenet to be? "))
print(power_base(base, exponent))