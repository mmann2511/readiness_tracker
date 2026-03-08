from scoring_tables import ScoringTables

class Operator():

    def __init__(self, name, rank, unit, flight = None, dnic = False, pt_clear = False, training = True):
        self.name = name
        self.rank = rank
        self.unit = unit
        self.flight = flight
        self.dnic = dnic
        self.pt_clear = pt_clear
        self.training = training

        # PFT attributes
        self.taken = False
        self.total_score = 0
        self.test_passed = False
        self.last_cardio_choice = None
        self.scores = {
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


    def is_ready(self):
        return self.dnic == False and self.pt_clear == True and self.test_passed == True  
    

    def __str__(self):
        return f"""
        Name: {self.name}
        Rank: {self.rank}
        Unit: {self.unit}
        Flight: {self.flight}
        Medical Status: {'GREEN' if self.is_ready() else 'RED'}
        PFT: {'PASS' if self.test_passed else 'FAIL'}
        """
    
    def record_test(self, scores: dict, cardio_choice: str):
        self.taken = True
        self.last_cardio_choice = cardio_choice

        for key, value in scores.items():
            
            for innerKey, innerValue in value.items():
                score = self.get_score(key, innerValue)

                self.scores[key]['score'] = score
                self.scores[key][innerKey] = innerValue
                self.scores[key]["pass_fail"] = 'PASS' if score else 'FAIL'

        for key, value in self.scores.items():
            if value['score']:
                self.total_score += value['score']

        self.test_passed = True
        for key, value in self.scores.items():
            if value['pass_fail']== 'FAIL':
                self.test_passed = False

                     
            
            


    ## Helper Method ##
    def get_score(self, event, raw_value):

        table = getattr(ScoringTables, event)

        for range_tuple, points in table.items():
            # single value "this value or higher"
            if len(range_tuple) == 1:
                if raw_value >= range_tuple[0]:
                    return points
                
            else:
                if range_tuple[0] <= raw_value <= range_tuple[1]:
                    return points

        return False 
    

    def to_dict(self):
        return {
            "name": self.name,
            "rank": self.rank,
            "unit": self.unit,
            "flight": self.flight,
            "dnic": self.dnic,
            "pt_clear": self.pt_clear,

            # PFT INFO

            "taken": self.taken,
            "total_score": self.total_score,
            "test_passed": self.test_passed,
            "last_cardio_choice": self.last_cardio_choice,

            # Individual Scores
            "scores": self.scores
        }

