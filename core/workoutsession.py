import datetime
import uuid
from .exercises import ExerciseLog, WeightedExerciseLog, TimeExerciseLog
from .workoutplan import WorkoutPlan

class WorkoutSession:
    def __init__(self, date: datetime.date, workout_plan_id: str | None = None):
        self.session_id = str(uuid.uuid4())
        self.date = date
        self.workout_plan_id = workout_plan_id
        self.exercises_list = []
        self.is_completed = False
        
    def add_exercise_log(self, exercise):
        self.exercises_list.append(exercise)   
    
    def remove_exercise_log(self, list_index: int):
        if 0 <= list_index < len(self.exercises_list):
            self.exercises_list.pop(list_index)    
    
    def complete_session(self):
        self.is_completed = True
    
    
    #TODO to jest do zmienienia na razie to tylko place holer to wazne!!!!    
    def __str__(self):
        status = "ZAKOŃCZONY" if self.is_completed else "W TRAKCIE"
        plan_info = f"Szablon: {self.workout_plan_id}" if self.workout_plan_id else "Własny trening"
        
        header = f"=== Sesja ({status}) | Data: {self.date} | {plan_info} ==="
        logs = [str(log) for log in self.exercises_list]
        
        return "\n".join([header] + logs)
    
    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "date": str(self.date), # WAŻNE: JSON nie rozumie obiektów daty, musisz zamienić to na tekst (str)!
            "workout_plan_id": self.workout_plan_id,
            "exercises": [exercise.to_dict() for exercise in self.exercises_list]
        }
        
    
        


#TODO metoda zeby formatowac jednostke trenigowa na jsona
