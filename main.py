from data_manager import load_data


def main_menu():

    menu = """
    MAIN MENU
    1. Unit commands
    2. Flight commands
    3. Operator commands
    4. Save and exit
    """
    
    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            unit_commands()
        elif choice == "2":
            flight_commands()
        elif choice == "3":
            operator_commands()
        else:
            break
    
def unit_commands():
    menu = """
    Unit commands coming soon
    1. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            return   

def flight_commands():
    menu = """
    Flight commands coming soon
    1. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            return

def operator_commands():
    menu = """
    Operator commands coming soon
    1. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            return

def main():
    data = load_data()

    if data is None:
        main_menu()









if __name__ == "__main__":
    main()