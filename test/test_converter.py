from newton.converter import mass_to_weight, weight_to_mass
from nose.tools import raises

def test_mass_to_weight():
	weight = mass_to_weight(10,9.81)
	assert weight == 98.1
	
@raises(SystemExit)
def test_negative_mass():
	weight = mass_to_weight(-1,10)
	
def test_weight_to_mass():
	mass = weight_to_mass(98.1,9.81)
	assert mass == 10
	
@raises(SystemExit)
def test_negative_weight():
	mass = weight_to_mass(-10,9.81)
	
@raises(SystemExit)
def test_negative_gravity_to_mass():
	mass = weight_to_mass(10,0)