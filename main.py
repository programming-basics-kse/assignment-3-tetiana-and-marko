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

def arguments_validation(input_file, country, year=None):
    year_flag = country_flag = False
    if not os.path.exists(input_file):
        print("There is no such input file")
        return False

    if args.overall:
        for i in country:
            for j in range(len(data)):
                if i == data[j][6] or i == data[j][7] or args.total:
                    country_flag = True
        year_flag = True

    for i in range(len(data)):
        if country == data[i][6] or country == data[i][7] or args.total:
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


# TOTAL
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
        if not totals[j].count("Bronze") == 0 and not totals[j].count("Silver") == 0 and not totals[j].count(
                "Gold") == 0:
            print(
                f"{j}  Bronze:{totals[j].count('Bronze')} Silver:{totals[j].count('Silver')} Gold:{totals[j].count('Gold')}")


# OVERALL
def overall_sorter(countries):
    overall = {}
    sorted_result = {}

    for c in countries:
        overall[c] = {}
        for b in data:
            if b[6] == c or b[7] == c:
                year = b[9]
                medals_count = b.count('Bronze') + b.count('Silver') + b.count('Gold')
                if year in overall[c]:
                    overall[c][year] += medals_count
                else:
                    overall[c][year] = medals_count

    for c in countries:
        if overall[c]:
            year, maxi = max(overall[c].items(), key=lambda x: x[1])
            sorted_result[c] = {year: maxi}

    return sorted_result


def print_overall(countries):
    overall = overall_sorter(countries)
    for i in overall:
        print(f"{i} {list(overall[i].keys())[0]} {list(overall[i].values())[0]}")


# MEDALS
def print_medalists(country, year):
    counter = 0
    medals_count = []
    for i in range(len(data)):
        if counter < 10:
            if (data[i][6] == country or data[i][7] == country) and year == data[i][9] and data[i][-1] != 'NA':
                print(f"{data[i][1]}, {data[i][12]}, {data[i][-1]}")
                counter += 1
        else:
            break
    for l in data:
        if (l[6] == country or l[7] == country) and year == l[9]:
            if l[-1] != 'NA':
                medals_count.append(l[-1])

    print(f"Total numbers of medal:{len(medals_count)}  Gold:{medals_count.count('Gold')}  Silver:{medals_count.count('Silver')}  Bronze:{medals_count.count('Bronze')}")


def write_output(country, year, type):
    with open(f"{args.output}", "wt") as file:
        if type == args.medals:
            medals_count = []
            counter = 0
            for i in range(len(data)):
                if counter < 10:
                    if (data[i][6] == country or data[i][7] == country) and year == data[i][9] and data[i][
                        -1] != 'NA':
                        file.write(f"{data[i][1]}, {data[i][12]}, {data[i][-1]}")
                        counter += 1
                        file.write("\n")
                else:
                    break
            for l in data:
                if (l[6] == country or l[7] == country) and year == l[9]:
                    if l[-1] != 'NA':
                        medals_count.append(l[-1])
            file.write(f"Total numbers of medal:{len(medals_count)}  Gold:{medals_count.count('Gold')}  Silver:{medals_count.count('Silver')}  Bronze:{medals_count.count('Bronze')}")

        if type == args.total:
            totals = total_dictionary(year)
            for j in totals:
                if not totals[j].count("Bronze") == 0 and totals[j].count("Silver") == 0 and totals[j].count(
                        "Gold") == 0:
                    file.write(
                        f"{j}  Bronze:{totals[j].count('Bronze')} Silver:{totals[j].count('Silver')} Gold:{totals[j].count('Gold')}")
                    file.write("\n")

        if type == args.overall:
            overall = overall_sorter(country)
            for i in overall:
                file.write(f"{i} {list(overall[i].keys())[0]} {list(overall[i].values())[0]}")
                file.write("\n")

    file.close()

def is_continue():
    answ=""
    print("Do you want to continue?")
    while answ.lower()!="y" and answ.lower()!="n":
        answ=input(">> ")
    if answ=="y":
        return True
    else:
        return False

def choose_mode()->str:
    modes=["medals","total","overall"]
    print("You have 4 options (enter name of the command(medals)): ")
    print("-medals (get medalists by country and year)")
    print("-total (get medalists by year)")
    print("-overall (get max amount of medalists by countries names)")
    mode = ""
    while mode not in modes:
        mode = input(">> ")
        mode = mode.replace(" ", "")
        mode = mode.replace("-", "")
        mode = mode.lower()
    return mode
def enter_medals_data():
    country=input("Enter country: ")
    year=input("Enter year: ")
    return country,year
def enter_total_data():
    year = input("Enter year: ")
    return year
def enter_overall_data():
    print("Enter names of countries(USA Canada): ")
    countries=input(">> ").split(" ")
    return countries
def is_save_data():
    answ = ""
    print("Do you want to save data in file?")
    while answ.lower() != "y" and answ.lower() != "n":
        answ = input(">> ")
    if answ == "y":
        return True
    else:
        return False


def interactive_mode():
    modes=["medals","total","overall"]
    print("----")
    while True:
        country = None
        mode=choose_mode()
        if mode==modes[0]:
            country,year=enter_medals_data()
            year=int(year)
            print_medalists(country, year)
            print_medalists("USA",1990)
        elif mode==modes[1]:
            year=enter_total_data()
            print_total(year)
        else:
            countries=enter_overall_data()
            print_overall(countries)

        if not is_continue():
            break
    if is_save_data():
        output_file=input("Enter file name: ")
        output_file=output_file.replace(" ","")




# PARSER
parser = argparse.ArgumentParser()
parser.add_argument('input', help="Filepath for an input file")
parser.add_argument('-medals', nargs=2, help="Argument to get medalists by country and year")
parser.add_argument('-total', help="Argument to get medalists by year")
parser.add_argument('-overall', nargs='+', help="Argument to get the year with the most medals")
parser.add_argument('-output', type=str, help="Filepath for an output file")
parser.add_argument('-interactive',action="store_true", help="Argument to switch to interactive mode")
args = parser.parse_args()

# LOAD DATA
data = get_data_from_file(args.input)

# MAIN

if args.interactive:
    interactive_mode()

if args.medals:
    country, year = args.medals
    if year.isdigit():
        year = int(year)
elif args.total:
    year = args.total
    country = None
    if year.isdigit():
        year = int(year)

elif args.overall:
    country = args.overall
    year = None


if arguments_validation(args.input, country, year):
    if args.medals:
        print_medalists(country, year)
        if args.output:
            write_output(country, year, args.medals)
    elif args.total:
        print_total(year)
        if args.output:
            write_output(country, year, args.total)
    elif args.overall:
        print_overall(country)
        if args.output:
            write_output(country, year, args.overall)
else:
    print("Try again")
