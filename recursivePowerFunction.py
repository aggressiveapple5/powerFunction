def power_base(base, exponent):
	
	 
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	
	return base * power_base(base , exponent - 1)
	
	
print(power_base(3, 2))
print(power_base(5, 4))
print(power_base(3, 3))