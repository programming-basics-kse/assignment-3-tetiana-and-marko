import os
import argparse
import sys

LIST_NUM = 10


def get_data_from_file(name):
    data = []
    with open(os.getcwd() + fr"\{name}", "r") as file:
        next(file)
        for row in file:
            a = [int(i) if i.isdigit() else i.replace('"', '') for i in row[:-1].split(",")]
            data.append(a)
    return data


def arguments_validation(input_file, medalist, country, year, output_file):
    if not os.path.exists(input_file):
        print("There is no such input file")
        return False

    year_flag = country_flag = False
    for i in range(len(data)):
        if country == data[i][6] or country == data[i][7]:
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


def print_medalists(country, year):
    counter = 0
    for i in range(len(data)):
        if counter < 10:
            if (data[i][6] == country or data[i][7] == country) and year == data[i][9]:
                print(*data[i], sep="; ")
                counter += 1
        else:
            break


def write_output(country, year):
    with open(f"{args.output}", "wt") as file:
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
    file.close()


parser = argparse.ArgumentParser()
parser.add_argument('input', help="Filepath for an input file")
parser.add_argument('-medals', action="store_true", required=True, help="Filepath for an input file")
parser.add_argument('country', type=str,
                    help="Country. The name can be entered both by full name (Team column) and by code")
parser.add_argument('year', type=int, help="The year of the Olympics")
parser.add_argument('-output', type=str, help="Filepath for an output file")
args = parser.parse_args()

data = get_data_from_file("athlete_events.csv")

if arguments_validation(args.input, args.medals, args.country, args.year, args.output):
    print_medalists(args.country, args.year)
    if args.output :
        write_output(args.country, args.year)
else:
    print("Try again")
