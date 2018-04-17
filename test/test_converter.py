from newton.converter import mass_to_weight

def test_mass_to_weight():
	weight = mass_to_weight(10)
	assert weight == 98.1