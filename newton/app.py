import argparse
from newton import converter

def main():
	parser = argparse.ArgumentParser(
		prog='newton',
		description='mass to weight converter')
	arggroup = parser.add_mutually_exclusive_group(required=True)
	arggroup.add_argument(
		'--mass', '-m',
		type=float,
		help='Mass in kg')
	arggroup.add_argument(
		'--weight', '-w',
		type=float,
		help='Weight in N')
	parser.add_argument(
		'--gravity', '-g',
		type=float,
		default=9.81,
		help='Graviational acceleration in m/s^2')
	args = parser.parse_args()
	if args.mass is not None:
		weight = converter.mass_to_weight(args.mass, args.gravity)
		print('Mass = %s kg -> Weight = %s N' % (args.mass,weight))
	elif args.weight is not None:
		mass = converter.weight_to_mass(args.weight, args.gravity)
		print('Weight = %s N -> Mass = %s kg' % (args.weight, mass))
	