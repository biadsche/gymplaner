#TODO funckjonalnosc zapiyswania treningow na telefonie
#TODO dodac funkcjonalnosc jakiegos goala
#TODO funkcjonalnosc agenta do jakiegos planowania albo cos
#TODO mozliwosc resetowania goali

from core import ExerciseRepository, WorkoutHistoryRepository
from cli import menu




def main():
    exercise_repo = ExerciseRepository()
    workout_repo = WorkoutHistoryRepository()
    menu(exercise_repo, workout_repo)
    



if __name__ == "__main__":
    main()