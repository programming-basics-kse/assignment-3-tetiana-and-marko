import os
import argparse
import sys
from interactive import interactive_mode

LIST_NUM = 10

def get_data_from_file(name):
    data = []
    with open(os.getcwd() + fr"\{name}", "r") as file:
        next(file)
        for row in file:
            a = [int(i) if i.isdigit() else i.replace('"', '') for i in row[:-1].split(",")]
            data.append(a)
    return data

def arguments_validation(input_file, country, year, output_file):
    if not os.path.exists(input_file):
        print("There is no such input file")
        return False
    year_flag = country_flag = False
    for i in range(len(data)):
        if country == data[i][6] or country==data[i][7] or args.total:
            country_flag = True
        if year == data[i][9]:
            year_flag = True
    if year_flag and country_flag:
        return True
    if not country_flag:
        print(f"{country} is not in dataset!(Country invalid)")
    if not year_flag:
        print(f"{year} is not in dataset!(Year invalid)")
    return False

def total_dictionary(year):
    totals = {}
    for i in data:
        if year == i[9]:
            if not i[6] in totals:
                totals[i[6]] = []
                totals[i[6]].append(i[-1])
            else:
                totals[i[6]].append(i[-1])
    return totals

def print_total(year):
    totals = total_dictionary(year)
    for j in totals:
        if not totals[j].count("Bronze") == 0 and totals[j].count("Silver") == 0 and totals[j].count("Gold") == 0:
            print(
                f"{j}  Bronze:{totals[j].count('Bronze')} Silver:{totals[j].count('Silver')} Gold:{totals[j].count('Gold')}")

def print_medalists(country, year):
    counter = 0
    for i in range(len(data)):
        if counter < 10:
            if (data[i][6] == country or data[i][7] == country) and year == data[i][9]:
                print(f"{data[i][1]}, {data[i][12]}, {data[i][14]}")
                counter += 1
        else:
            break

def write_output(country, year, type):
    with open(f"{args.output}", "wt") as file:
        if type == args.medals:
            counter = 0
            for i in range(len(data)):
                if counter < 10:
                    if (data[i][6] == country or data[i][7] == country) and year == data[i][9]:
                        for j in data[i]:
                            file.write(f"{j}, ")
                        counter += 1
                        file.write("\n")
                else:
                    break
        if type == args.total:
            totals = total_dictionary(year)
            for j in totals:
                if not totals[j].count("Bronze") == 0 and totals[j].count("Silver") == 0 and totals[j].count(
                        "Gold") == 0:
                    file.write(
                        f"{j}  Bronze:{totals[j].count('Bronze')} Silver:{totals[j].count('Silver')} Gold:{totals[j].count('Gold')}")
                    file.write("\n")
    file.close()



#PARSER
parser = argparse.ArgumentParser()
parser.add_argument('input', help="Filepath for an input file")
parser.add_argument('-medals',nargs=2, help="Argument to get medalists by country and year")
parser.add_argument('-total', help="Argument to get medalists by year")
parser.add_argument('-output', type=str, help="Filepath for an output file")
parser.add_argument('-interactive',nargs='*', help="Argument to switch to interactive mode")
args = parser.parse_args()

#LOAD DATA
data = get_data_from_file("athlete_events.csv")

#MAIN
if args.interactive:
    interactive_mode()
if args.medals:
    country,year=args.medals
else:
    year=args.total
    country=None
if year.isdigit():
    year = int(year)

if arguments_validation(args.input, country, year, args.output):
    if args.medals:
        print_medalists(country, year)
        if args.output:
            write_output(country, year, args.medals)
    elif args.total:
        print_total(year)
        if args.output:
            write_output(country, year, args.total)
else:
    print("Try again")
