from argparse import *

#Argaparse calculator

parser = ArgumentParser(description="Welcome to the calculator. Use this to do some calculations.")

parser.add_argument("calculation_type",type=str, help="Specify which type of calculation you wish to do.")
parser.add_argument("number_1", type=int,help="The first number")
parser.add_argument("number_2", type=int,help="The second number")


# Parsing aurguments

args = parser.parse_args()

print(args.number_1)

if args.calculation_type == "add":
    print(args.number_1 + args.number_2)