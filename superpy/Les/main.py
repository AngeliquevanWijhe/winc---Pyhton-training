from argparse import *
from functions import (addition, subtraction, time)

#Argaparse calculator

parser = ArgumentParser(description="Welcome to the calculator. Use this to do some calculations.")
subparsers = parser.add_subparsers(dest="command")

# Create calculator parser
calculator_parser = subparsers.add_parser("calculate", help="Used to calculate")
calculator_parser.add_argument("calculation_type", type=str, help="Specify which type of calculation you wish to do.")
calculator_parser.add_argument("number_1", type=int,help="The first number")
calculator_parser.add_argument("number_2", type=int,help="The second number")

time_parser = subparsers.add_parser("time", help="Display current date and time.")

# Parsing aurguments

args = parser.parse_args()

# print(args.number_1)

if args.command == "calculate":
    if args.calculation_type == "add":
        outcome = addition(args.number_1,args.number_2)
    
    elif args.calculation_type == "subtract":
        outcome = subtraction(args.number_1,args.number_2)

elif args.command == "time":
    outcome = time()

print(f"The outcome is {outcome}")