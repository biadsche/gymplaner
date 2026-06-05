from enum import StrEnum
class MuscleGroup(StrEnum):
    CHEST_GENERAL = "CHEST_GENERAL" 
    CHEST_UPPER = "CHEST_UPPER"      
    CHEST_LOWER = "CHEST_LOWER"      

  
    FRONT_DELTS = "FRONT_DELTS"      
    SIDE_DELTS = "SIDE_DELTS"         
    REAR_DELTS = "REAR_DELTS"        

  
    BACK_GENERAL = "BACK_GENERAL"    
    LATS = "LATS"                     
    TRAPS = "TRAPS"                  
    LOWER_BACK = "LOWER_BACK"        
    RHOMBOIDS = "RHOMBOIDS"           
   
    QUADS = "QUADS"                  
    HAMSTRINGS = "HAMSTRINGS"        
    GLUTES = "GLUTES"              
    CALVES = "CALVES"                 


    BICEPS = "BICEPS"                 
    TRICEPS = "TRICEPS"               
    FOREARMS = "FOREARMS"             


    ABS = "ABS"                       
    OBLIQUES = "OBLIQUES"             
    CORE_GENERAL = "CORE_GENERAL"     
    
    @classmethod
    def get_grouped(cls) -> dict:
        return {
            "CHEST": [cls.CHEST_GENERAL, cls.CHEST_UPPER, cls.CHEST_LOWER],
            "SHOULDERS": [cls.FRONT_DELTS, cls.SIDE_DELTS, cls.REAR_DELTS],
            "BACK": [cls.BACK_GENERAL, cls.LATS, cls.TRAPS, cls.LOWER_BACK, cls.RHOMBOIDS],
            "LEGS": [cls.QUADS, cls.HAMSTRINGS, cls.GLUTES, cls.CALVES],
            "ARMS": [cls.BICEPS, cls.TRICEPS, cls.FOREARMS],
            "CORE & ABS": [cls.ABS, cls.OBLIQUES, cls.CORE_GENERAL]
        }




class SetLoad:
    def __init__(self, reps: int, load: float):
        self.reps = reps
        self.load = load
    
    def sum_load(self) -> float:
        return self.reps * self.load
    
    def __str__(self) -> str:
        return f"{self.reps} x {self.load}kg"
    
    def to_dict(self) -> dict:
        return {
            "reps": self.reps,
            "load": self.load
        }
    

class SetTime:
    def __init__(self, time: float):
        self.time = time

    def __str__(self) -> str:
        return f"{self.time}s"
    def to_dict(self) -> dict:
        return {
            "time": self.time
        }




class ExerciseLog:
    def __init__(self, exercise_id):
        self.exercise_id = exercise_id
    
    def __str__(self) -> str:
        return f"ID: {self.exercise_id}]"



class WeightedExerciseLog(ExerciseLog):
    def __init__(self, exercise_id: str):
        super().__init__(exercise_id)
        self.sets_list = []

    def add_set(self, set_load: SetLoad):
        self.sets_list.append(set_load)
        
    def __str__(self) -> str:
        sets_str = ", ".join([str(s) for s in self.sets_list])
        return f"Log (Weighted)[ID: {self.exercise_id}] | Sets: {sets_str}"
    def to_dict(self) -> dict:
        return {
            "exercise_id": self.exercise_id,
            "sets": [single_set.to_dict() for single_set in self.sets_list] 
        }
    


class TimeExerciseLog(ExerciseLog):
    def __init__(self, exercise_id: str):
        super().__init__(exercise_id)
        self.sets_list = []
        
    def add_set(self, set_time: SetTime):
        self.sets_list.append(set_time)
        
    def __str__(self) -> str:
        sets_str = ", ".join([str(s) for s in self.sets_list])
        return f"Log (Time) [ID: {self.exercise_id}] | Sets: {sets_str}"
   
    def to_dict(self) -> dict:
        return {
            "exercise_id": self.exercise_id,
            "sets": [single_set.to_dict() for single_set in self.sets_list] 
        }
