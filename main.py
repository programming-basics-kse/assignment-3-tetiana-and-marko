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


def arguments_validation(input_file, country, year, output_file):
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

def write_overall():
    pass


def print_medalists(country, year):
    counter = 0
    for i in range(len(data)):
        if counter < 10:
            if (data[i][6] == country or data[i][7] == country) and year == data[i][9]:
                print(f"{data[i][1]}, {data[i][12]}, {data[i][-1]}")
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
        if type == args.overall:
            overall = overall_sorter(country)
            for i in overall:
                file.write(f"{i} {list(overall[i].keys())[0]} {list(overall[i].values())[0]}")
                file.write("\n")

    file.close()


# PARSER
parser = argparse.ArgumentParser()
parser.add_argument('input', help="Filepath for an input file")
parser.add_argument('-medals', nargs=2, help="Argument to get medalists by country and year")
parser.add_argument('-total', help="Argument to get medalists by year")
parser.add_argument('-overall', nargs='+', help="Argument to get the year with the most medals")
parser.add_argument('-output', type=str, help="Filepath for an output file")

args = parser.parse_args()

# LOAD DATA
data = get_data_from_file("athlete_events.csv")

# MAIN
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


if arguments_validation(args.input, country, year, args.output):
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
