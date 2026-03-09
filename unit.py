from flight import Flight

class Unit():

    def __init__(self, name):
        self.name = name
        self.flights = {}
    

    def add_flight(self, flight):
        flight.unit = self.name
        self.flights[flight.name] = flight

    
    def get_flight(self, name):
        if name in self.flights:
            return self.flights[name]
        else:
            return None


    def unit_average(self):
        if len(self.flights) == 0:
            return None

        result = 0

        for name, flight in self.flights.items():
            result += flight.flight_average()
            


        return result / len(self.flights)    

    def unit_readiness(self):
        if len(self.flights) == 0:
            return None

        result = 0

        for name, flight in self.flights.items():
            result += flight.readiness_rate()

        return result / len(self.flights)
    
    def to_dict(self):
        
        unit_dict = {}

        for name, flight in self.flights.items():
            unit_dict[name] = flight.to_dict()

        return {
            "name": self.name,
            "flights": unit_dict
        }    
    

if __name__ == "__main__":
    unit = Unit("7th ASOS")
    print(unit.get_flight("Alpha"))
    alpha = Flight("Alpha")
    bravo = Flight("Bravo")
    charlie = Flight("Charlie")
    unit.add_flight(alpha)
    unit.add_flight(bravo)
    unit.add_flight(charlie)
    print(unit.get_flight("Alpha"))
    print(alpha.unit)
    print(alpha.to_dict)