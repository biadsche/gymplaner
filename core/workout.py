from .models import Exercise, WeightedExercise, TimeExercise


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises_list = []
    
    def add_exercise(self, exercise):
        self.exercises_list.append(exercise)

    def __str__(self) -> str:
        header = f"Workout: {self.name}"
        exercises = [str(ex) for ex in self.exercises_list]
        return "\n".join([header] + exercises)