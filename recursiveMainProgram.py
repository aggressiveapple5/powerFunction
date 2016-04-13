import recursivePowerFunction


#Tests of int and float functions
print("Tests of int and float functions: ")
base = recursivePowerFunction.float_input("What do you want as your base?")
exponent = recursivePowerFunction.int_input("What do you want as your exponent?")
print("Base: {}. Exponent {}. Answer {}.".format(base, exponent, recursivePowerFunction.power_base(base, exponent)))
		

print("Recursive power function test cases.")		
print("2 to the 3 power is: {}".format(recursivePowerFunction.power_base(2, 3)))
print("4 to the 1 power is: {}".format(recursivePowerFunction.power_base(4, 1)))
print("0 to the 4 power is: {}".format(recursivePowerFunction.power_base(0, 4)))
print("32 to the 0 power is: {}".format(recursivePowerFunction.power_base(32, 0)))
print("234 to the 5 power is: {}".format(recursivePowerFunction.power_base(234, 5)))
print("2.7 to the 3 power is: {}".format(recursivePowerFunction.power_base(2.7, 3)))