import argparse

parser = argparse.ArgumentParser(description="Process a simple argument.")
parser.add_argument("arg", help="The main argument for the script.")
args = parser.parse_args()

if args.arg == 'foo':
    print('You provided foo!')
else:
    print(f'You provided {args.arg}')