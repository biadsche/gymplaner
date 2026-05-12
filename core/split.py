from .workoutplan import WorkoutPlan

class Split:
    def __init__(self, name):
        self.name = name
        self.workouts_list = []
    
    def add_workout(self, workout):
        self.workouts_list.append(workout)


    def __str__(self) -> str:
        header = f"Split: {self.name}"
        workouts = [f"- {w.name} (Dzień: {w.weekday})" for w in self.workouts_list]
        return "\n".join([header] + workouts)