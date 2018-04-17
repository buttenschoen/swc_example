import sys

def mass_to_weight(mass, gravity):
	try:
		assert mass >= 0
		weight = mass * gravity
	except AssertionError:
		print('Mass cannot be negative!')
		sys.exit(1)
	else:
		return round(weight,2)
		
def weight_to_mass(weight, gravity):
	try:
		assert weight >= 0
		mass = weight / gravity
	except ZeroDivisionError:
		print('Space brings total weightlessness!')
		sys.exit(1)
	except AssertionError:
		print('Weight cannot be negative, gravity has to be positive!')
		sys.exit(1)
	else:
		return round(mass, 2)