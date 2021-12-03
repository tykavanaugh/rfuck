variable_fizzybuzz = 50
variable_frank = 70
variable_ian = 73
variable_zack = 90
variable_bob = 66
variable_union = 85
variable_nest = 0
variable_third = 3
variable_fifth = 5
variable_cat = 1
variable_my_car = 32
while variable_fizzybuzz:
	variable_party = variable_fizzybuzz % variable_third
	variable_theclub = variable_fizzybuzz % variable_fifth
	variable_party = variable_party == variable_nest
	variable_theclub = variable_theclub == variable_nest
	if variable_party:
		if variable_theclub:
			print(chr(variable_frank),end="")
			print(chr(variable_ian),end="")
			print(chr(variable_zack),end="")
			print(chr(variable_zack),end="")
			print(chr(variable_bob),end="")
			print(chr(variable_union),end="")
			print(chr(variable_zack),end="")
			print(chr(variable_zack),end="")
		print(chr(variable_frank),end="")
		print(chr(variable_ian),end="")
		print(chr(variable_zack),end="")
		print(chr(variable_zack),end="")
	if variable_theclub:
		print(chr(variable_bob),end="")
		print(chr(variable_union),end="")
		print(chr(variable_zack),end="")
		print(chr(variable_zack),end="")
	print(chr(variable_my_car),end="")
	variable_fizzybuzz = variable_fizzybuzz - variable_cat
