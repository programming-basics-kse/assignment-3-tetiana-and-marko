from itertools import count
from statistics import mean
def is_continue():
    answ = ""
    print("Do you want to continue?")
    while answ.lower() != "y" and answ.lower() != "n":
        answ = input(">> ")
    if answ == "y":
        return True
    else:
        return False


def country_validation(data,country):
    for i in range(len(data)):
        if country == data[i][6] or country == data[i][7]:
            return True
    return False


def count_medals(data,country):
    years_places ={}
    years_medals={}
    years_gold={}
    years_silver ={}
    years_bronze = {}

    for i in range(len(data)):
        if data[i][6] == country or data[i][7] == country:
            years_places[data[i][9]]=data[i][11]
            if data[i][-1] != 'NA':
                if data[i][9] not in years_medals.keys():
                    years_medals[data[i][9]]=1
                else:
                    years_medals[data[i][9]]+=1
                if data[i][-1]=="Gold":
                    if data[i][9] not in years_gold.keys():
                        years_gold[data[i][9]]=1
                    else:
                        years_gold[data[i][9]]+=1
                elif data[i][-1]=="Silver":
                    if data[i][9] not in years_silver.keys():
                        years_silver[data[i][9]]=1
                    else:
                        years_silver[data[i][9]]+=1
                else:
                    if data[i][-1] not in years_bronze.keys():
                        years_bronze[data[i][9]]=1
                    else:
                        years_bronze[data[i][9]]+=1

    return years_places,years_medals,years_gold,years_silver,years_bronze

def print_interactive(data,country):
    years_places,years_medals,years_gold,years_silver,years_bronze=count_medals(data,country)
    print(*years_places.keys())
    first_year=min(years_places.keys())
    average_gold=int(mean(years_gold.values()))
    average_silver=int(mean(years_silver.values()))
    average_bronze = int(mean(years_bronze.values()))

    print(f"First Olympiad: {first_year}, {years_places[first_year]}")
    print(f"Most successful Olympiad(number of medals): {max(years_medals.values())}")
    print(f"Most unsuccessful Olympiad(number of medals): {min(years_medals.values())}")
    print(f"Average number of Gold medals: {average_gold}")
    print(f"Average number of Silver medals: {average_silver}")
    print(f"Average number of Bronze medals: {average_bronze}")

    output_data={
        "First Olympiad":f"{first_year}, {years_places[first_year]}",
        "Most successful Olympiad(number of medals)":max(years_medals.values()),
        "Most unsuccessful Olympiad(number of medals)":min(years_medals.values()),
        "Average number of Gold medals":average_gold,
        "Average number of Silver medals":average_silver,
        "Average number of Bronze medals":average_gold
    }
    return output_data

def is_save_data():
    answ = ""
    print("Do you want to save last data in file?")
    while answ.lower() != "y" and answ.lower() != "n":
        answ = input(">> ")
    if answ == "y":
        return True
    else:
        return False

def save_data(file_name,data):
    with open(f"{file_name}", "wt") as file:
        for key,value in data.items():
            file.write(f"{key}: {value}\n")

def interactive_mode(data):

    while True:
        country = ""
        while not country_validation(data,country):
            country = input("Enter country code: ")
        output_data=print_interactive(data,country)
        if not is_continue():
            break
    if is_save_data():
        output_file = input("Enter file name: ")
        output_file = output_file.replace(" ", "")
        save_data(output_file, output_data)
