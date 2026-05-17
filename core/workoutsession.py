import datetime
import uuid
from .exercises import Exercise, WeightedExercise, TimeExercise
from .workoutplan import WorkoutPlan

class WorkoutSession:
    def __init__(self, session_id: int, date : datetime, base_plan_name : str | None = None, is_completed = False):
        self.session_id = session_id or str(uuid.uuid4())
        self.date = date
        self.base_plan_name = base_plan_name
        self.exercises_list = []
        self.is_completed = is_completed
        
    def add_exercise(self, exercise):
        if self.base_plan_name:
            for 
        self.exercises_list.append(exercise)   
        
    
        


#TODO metoda zeby formatowac jednostke trenigowa na jsona
