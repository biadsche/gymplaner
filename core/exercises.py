from enum import StrEnum
class MuscleGroup(StrEnum):
    # Klatka piersiowa (Chest)
    CHEST_GENERAL = "CHEST_GENERAL"   # Ogólnie klatka (np. płaskie wyciskanie)
    CHEST_UPPER = "CHEST_UPPER"       # Górna część klatki (np. wyciskanie na skosie dodatnim)
    CHEST_LOWER = "CHEST_LOWER"       # Dolna część klatki (np. dipy)

    # Barki (Shoulders / Deltoids)
    FRONT_DELTS = "FRONT_DELTS"       # Przedni akton barku (np. OHP)
    SIDE_DELTS = "SIDE_DELTS"         # Boczny akton barku (np. wznosy bokiem)
    REAR_DELTS = "REAR_DELTS"         # Tylny akton barku (np. face pull)

    # Plecy (Back)
    BACK_GENERAL = "BACK_GENERAL"     # Ogólnie plecy 
    LATS = "LATS"                     # Mięsień najszerszy grzbietu (np. podciąganie)
    TRAPS = "TRAPS"                   # Mięsień czworoboczny / "kaptury" (np. szrugsy)
    LOWER_BACK = "LOWER_BACK"         # Prostowniki / dół pleców (np. martwy ciąg, ławka rzymska)
    RHOMBOIDS = "RHOMBOIDS"           # Mięśnie równoległoboczne (środek pleców)

    # Nogi (Legs)
    QUADS = "QUADS"                   # Czworogłowe / przód uda (np. przysiady, wyprosty)
    HAMSTRINGS = "HAMSTRINGS"         # Dwugłowe / tył uda (np. martwy ciąg na prostych nogach, uginanie)
    GLUTES = "GLUTES"                 # Pośladki (np. hip thrusty)
    CALVES = "CALVES"                 # Łydki (np. wspięcia na palce)

    # Ramiona (Arms)
    BICEPS = "BICEPS"                 # Biceps
    TRICEPS = "TRICEPS"               # Triceps
    FOREARMS = "FOREARMS"             # Przedramiona


    ABS = "ABS"                       # Mięsień prosty brzucha ("kaloryfer")
    OBLIQUES = "OBLIQUES"             # Mięśnie skośne brzucha
    CORE_GENERAL = "CORE_GENERAL"     # Ogólnie mięśnie głębokie (np. plank)




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
