#TODO ten workoutplan moznaby przepisac bo to po chuju jest napisane

class WorkoutPlan:
    def __init__(self, name : str, weekday: str):
        self.name = name
        self.weekday = weekday
        self.exercises_list = []
    
    def add_exercise(self, exercise):
        self.exercises_list.append(exercise)

    def __str__(self) -> str:
        header = f"Workout: {self.name}, {self.weekday}"
        exercises = [str(ex) for ex in self.exercises_list]
        return "\n".join([header] + exercises)