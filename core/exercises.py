class SetLoad:
    def __init__(self, reps: int, load: float):
        self.reps = reps
        self.load = load
    
    def sum_load(self) -> float:
        return self.reps * self.load
    
    def __str__(self) -> str:
        return f"{self.reps} x {self.load}kg"
    

class SetTime:
    def __init__(self, time: float):
        self.time = time

    def __str__(self) -> str:
        return f"{self.time}s"





class Exercise:
    def __init__(self, name:str, note: str = ""):
        self.name = name
        self.note = note
    
    def __str__(self) -> str:
        if self.note:
            return f"{self.name} - {self.note}"
        else:
            return f"{self.name}"



class WeightedExercise(Exercise):
    def __init__(self, name: str, note: str = ""):
        super().__init__(name, note)
        self.sets_list = []

    def add_set(self, set_load: SetLoad):
        self.sets_list.append(set_load)


class TimeExercise(Exercise):
    def __init__(self, name : str, note: str = ""):
        super().__init__(name, note)
        self.sets_list = []
    def add_set(self, set_time: SetTime):
        self.sets_list.append(set_time) 

