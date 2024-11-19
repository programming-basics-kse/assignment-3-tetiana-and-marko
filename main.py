import os
import argparse
import sys

def get_data_from_file(name):
    data = []
    with open(os.getcwd() + fr"\{name}", "r") as file:
        next(file)
        for row in file:
            a = [int(i) if i.isdigit() else i for i in row[:-1].split(";")]
            data.append(a)
    return data


parser=argparse.ArgumentParser()
parser.add_argument('input', help="Filepath for an input file")
parser.add_argument('-medals',action="store_true",required=True, help="Filepath for an input file")
parser.add_argument('country',type=str, help="Country. The name can be entered both by full name (Team column) and by code")
parser.add_argument('year',type=int, help="The year of the Olympics")
parser.add_argument('-output',type=str, help="Filepath for an output file")

args=parser.parse_args()


"""
print ("The path is ", args.input)
print ("Flag value is ", args.medals)
print("Country: ", args.country)
print("Year", args.year)
print("output file", args.output)

data=get_data_from_file(args.input)

for i in range(10):
    print(*data[i])
"""