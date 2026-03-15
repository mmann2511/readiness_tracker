

class Flight():

    def __init__(self, name, unit = None):
        self.name = name.lower()
        self.roster = {}
        self.red_operators = {}
        self.unit = unit


    def add_operator(self, operator):
        operator.flight = self.name
        operator.unit = self.unit
        self.roster[operator.name] = operator


    def remove_operator(self, name):
        if name in self.roster:
            del self.roster[name]


    def transfer_operator(self, name, flight):
        if name in self.roster:
            transfer = self.roster.pop(name, None)
            flight.add_operator(transfer)
            # another flight


    def get_operator(self, name):
        if name in self.roster:
            return self.roster[name]
        else:
            return None   
        
    
    def flight_average(self):
        if len(self.roster) == 0:
            return 0    
        
        result = 0
        for name, operator in self.roster.items():
            result += operator.total_score

      

        return result / len(self.roster)  
    
    def readiness_rate(self):
        if len(self.roster) == 0:
            return None
        
        green_operators = 0

        for name, operator in self.roster.items():
            if operator.is_ready():
                green_operators += 1
            else:
                self.red_operators[name] = operator.to_dict()

        result = (green_operators / len(self.roster)) * 100
        
        return result

    def to_dict(self):

        flight_dict = {}

        for name, operator in self.roster.items():
            flight_dict[name] = operator.to_dict()

        return {
            "name": self.name,
            "roster": flight_dict,
        }
