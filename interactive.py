
def is_continue():
    answ=""
    print("Do you want to continue?")
    while answ.lower()!="y" and answ.lower()!="n":
        answ=input(">> ")
    if answ=="y":
        return True
    else:
        return False
def interactive_mode():
    while True:
        print("You have 4 options: ")
        print("1. -medals (get medalists by country and year)")
        print("2. -total (get medalists by year)")
        print("3. -overall")


        if not is_continue():
            break