import json
from unit import Unit
from flight import Flight
from sw_operator import Operator

def save_data(unit):
    with open("readiness_data.json", "w") as file:
        json.dump(unit.to_dict(), file, indent=4)


def load_data():
    try:
        with open("readiness_data.json", "r") as file:
            data = json.load(file)
            unit = Unit(data['name'])

            for name, flight_data in data['flights'].items():
                flight = Flight(name)
                unit.add_flight(flight)
                
                for name, operator_data in flight_data['roster'].items():
                    operator = Operator(
                        operator_data['name'],
                        operator_data['rank'],
                        operator_data['unit'],
                        operator_data['flight'],
                        operator_data['dnic'],
                        operator_data['pt_clear'],
                    )

                    operator.taken = operator_data['taken']
                    operator.total_score = operator_data['total_score']
                    operator.test_passed = operator_data['test_passed']
                    operator.last_cardio_choice = operator_data['last_cardio_choice']
                    operator.scores = operator_data['scores']

                    flight.add_operator(operator)

            return unit
    except FileNotFoundError:
        return None    
