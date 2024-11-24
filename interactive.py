from main import print_medalists
from main import print_overall
from main import print_total
from main import  write_output
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
    while True:
        mode=choose_mode()
        if mode==modes[0]:
            country,year=enter_medals_data()
            print_medalists(country, year)
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

