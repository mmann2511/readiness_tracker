from data_manager import load_data
from unit import Unit

def main_menu(unit):

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
            unit_commands(unit)
        elif choice == "2":
            flight_commands(unit)
        elif choice == "3":
            operator_commands(unit)
        else:
            break
    
def unit_commands(unit):
    menu = """
    Unit commands:
    1. Unit Average Test Score
    2. Unit Readiness
    3. Flight Information
    4. Add Flight
    5. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
               

def flight_commands(unit):
    menu = """
    Flight commands coming soon
    1. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            return

def operator_commands(unit):
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
    unit = load_data()
    if unit is None:
        name = input("What is the unit name? ")
        unit = Unit(name)
    
    main_menu(unit)









if __name__ == "__main__":
    main()
