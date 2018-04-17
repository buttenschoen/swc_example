import argparse
from newton import converter

def main():
	parser = argparse.ArgumentParser(
		prog='newton',
		description='mass to weight converter')
	parser.add_argument(
		'--mass', '-m',
		type=float,
		help='Mass in kg',
		required=True)
	args = parser.parse_args()
	print("Mass is %s kg" % args.mass)
	weight = converter.mass_to_weight(args.mass)
	print("Weight is %s N" % weight)