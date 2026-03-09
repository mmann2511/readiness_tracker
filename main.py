from data_manager import load_data, save_data
from unit import Unit
from flight import Flight
from sw_operator import Operator

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
        elif choice == "4":
            save_data(unit)
            print("Data saved. Goodbye!")
            break
        else:
            break
    
def unit_commands(unit):
    menu = """
    Unit commands:
    1. Unit Average Test Score
    2. Unit Readiness
    3. Flight Information
    4. Add Flight
    5. Unit Info
    6. Main Menu
    """   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            print(f"Unit Average: {unit.unit_average()}")
        elif choice == "2":
            print(f"Unit Readiness: {unit.unit_readiness()}")
        elif choice == "3":
            if not unit.flights:
                print("No flights in unit")
                print("Add Flights")
            else:
                flight_commands(unit)    
        elif choice == "4":
            name = input("What is the name of the flight? ")
            flight = Flight(name)
            unit.add_flight(flight)
            print("Flight Added")
        elif choice == "5":
            print(unit.to_dict())
        else:
            return
               

def flight_commands(unit):
    flight = flight_selection_menu(unit)

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
            print(f"{flight.name.title()} Flight average: {flight.flight_average()} ")
        elif choice == "2":
            print(f"{flight.name.title()} Flight readiness: {flight.readiness_rate()}")
        elif choice == "3":
            flight.readiness_rate()
            print(f"{flight.name.title()} Red Operators: {flight.red_operators}") 
        elif choice == "4":
            print("Operator Creation: ")
            name = input("Name: ")
            rank = input("Rank: ")
            operator = Operator(name, rank)

            flight.add_operator(operator)
            print(f"{operator.name.upper()} added to {flight.name.upper()} Flight")
        elif choice == "5":
            name = input("Name of Operator: ")
            flight.remove_operator(name.lower())
            print("Operator is removed.")
        elif choice == "6":
            print("Please choose transfer flight. ")
            trans_flight = flight_selection_menu(unit)
            name = input("Name of Operator: ")
            flight.transfer_operator(name.lower(), trans_flight)
            print(f"{name.upper()} transferred to {trans_flight.name.upper()} Flight")
        else:
            return


            

def flight_selection_menu(unit):
    print("Flights")
    print("------------")
    for name in unit.flights.keys():
        print(name.title())
    choice = input("\nSelect Flight: ")
    return unit.get_flight(choice.lower())
    
def operator_commands(unit):
    flight = flight_selection_menu(unit)
    name = input("Name of Operator: ")
    operator = flight.get_operator(name)


    menu = """
Operator commands
------------------------------
1. View operator profile
2. Green light operator (set ready)
3. Red light operator (set not ready)
4. Record Test
5. View Test Scores
6. Main Menu
"""   

    while True:
        print(menu)
        choice = input("Input: ")
        if choice == "1":
            print(operator)
        elif choice == "2":
            operator.dnic = False
            operator.pt_clear = True
            print("Status: Green")
        elif choice == "3":
            print("Please answer True or False questions below .")
            dnic = input("Has operator been DNIC? T/F: ")
            pt_clear = input("Has operator been cleared by Physical Therapist? T/F: ")
            test = input("Has operator passed their PT Test? T/F: ")

            if (dnic.lower() == "t" or dnic.lower() == "true"):
                operator.dnic = True
            if (pt_clear.lower() == "f" or pt_clear.lower() == "false"):
                operator.pt_clear = False
            if (test.lower() == "f" or test.lower() == "false"):
                operator.test_passed = False 
        elif choice == "4":
            print("Please Provide Test Scores Below")
            score_dict = {
            "ruck": {"pass_fail": None, "time": 0.0, "score": 0},
            "long_jump": {"pass_fail": None, "distance": 0, "score": 0},
            "agility_right": {"pass_fail": None, "time": 0.0, "score": 0},
            "agility_left": {"pass_fail": None, "time": 0.0, "score": 0},
            "deadlift": {"pass_fail": None, "weight": 0, "score": 0},
            "pull_ups": {"pass_fail": None, "reps": 0, "score": 0},
            "carry": {"pass_fail": None, "time": 0.0, "score": 0},
            "shuttle": {"pass_fail": None, "time": 0.0, "score": 0},
            "cardio": {"pass_fail": None, "time": 0.0, "score": 0},
            }

            cardio_choice = None
            for key in score_dict:
                print(f"Test {key.title()}")
                time_values = {"ruck", "agility_right", "agility_left", "carry", "shuttle"}
                if key in time_values:
                    score = input("Time in seconds: ")
                    score_dict[key]["time"] = float(score)
                elif key == "long_jump":
                    score = input("Length in inches: ")
                    score_dict[key]["distance"] = int(score)
                elif key == "deadlift":
                    score = input("Weight in lbs: ")
                    score_dict[key]["weight"] = int(score)
                elif key == "pull_ups":
                    score = input("Number of reps: ")
                    score_dict[key]["reps"] = int(score)    
                elif key == "cardio":
                    cardio_choice = input("Run or Swim? ")
                    score = input("Time in seconds: ")
                    score_dict[key]["time"] = float(score)


            print("Recording Test.....")
            operator.record_test(score_dict, cardio_choice)      
            print("Test Recorded")             

        elif choice == "5":
            for event, score in operator.scores.items():
                print(event, score)
        elif choice == "6":
            return




def main():
    unit = load_data()
    if unit is None:
        name = input("What is the unit name? ")
        unit = Unit(name)
    
    main_menu(unit)









if __name__ == "__main__":
    main()
