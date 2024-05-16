def menu_list(items):
    option = 1
    for choice in items:
        print(str(option) + "." + choice)
        option = option + 1
    print(str(option) + ".QUIT")
    choice = int(input("Choose an option:"))
    return int(choice)
