from data_manager import load_data
from unit import Unit
from flight import flight

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
            print(f"Unit Average: {unit.unit_average()}")
        elif choice == "2":
            print(f"Unit Readiness: {unit.unit_readiness()}")
        elif choice == "3":
            flight_commands(unit)
        elif choice == "4":
            name = input("What is the name of the flight? ")
            flight = Flight(name)
            unit.add_flight(flight)
            print("Flight Added")
        else:
            return
               

def flight_commands(unit):
    menu = """
    Flight commands:
    1. Flight score average
    2. Flight readiness 
    3. View Red Operators
    4. Add Operator
    5. Remove Operator
    6. Transfer Operator
    7. Back to Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            flight = flight_selection_menu(unit)
            print(f"{flight.name.upper()} Flight average: {flight.flight_average()} ")
            

def flight_selection_menu(unit):
    print("Flights: ")
    for name in unit.flights.keys():
        print(f"{name.upper()} Flight")
    choice = input("Flight: ")
    return unit.get_flight(choice.lower())
    
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
