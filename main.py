#TODO funckjonalnosc zapiyswania treningow na telefonie
#TODO dodac funkcjonalnosc jakiegos goala
#TODO funkcjonalnosc agenta do jakiegos planowania albo cos
#TODO mozliwosc resetowania goali

import sys
from core import (
    WeightedExerciseLog,
    SetLoad,
    TimeExerciseLog,
    SetTime,
    MuscleGroup,
    ExerciseRepository,
    Split,
    WorkoutHistoryRepository,
    WorkoutPlan,
    WorkoutSession
)

def initialize_app():
    history_repo = WorkoutHistoryRepository()
    exercise_repo = ExerciseRepository()
    return exercise_repo, history_repo    

def main_loop(history_repo, exercise_repo):
    while True:
        print("\n1-Log Workout, 2-Create a workout, 3-Add Exercise")
        user_input = input("Wybór: ").strip()
        
        if user_input == "3":
            print("Podaj nazwe cwiczenia:")
            exercise_name = input()
            print("Podaj czy to jest cwiczenie z ciezarem (Tak/Nie):")
            exercise_type = input()
            print("Podaj na jakie grupy miesniowe jest to cwiczenie:")
            exercise_targeted_muscles = input()
            print("Notatka do cwiczenia (opcjonalna):")
            note = input()
            
            # Zmiana: wywołanie metody na instancji (exercise_repo)
            new_exercise = exercise_repo.add_exercise(
                exercise_name, 
                exercise_type, 
                exercise_targeted_muscles, 
                note
            )
            print(f"\n[SUKCES] Dodano ćwiczenie: {exercise_name}")

def main():
    try:
        # Zmiana: jednoczesne rozpakowanie zmiennych (kolejność zgodna z return w initialize_app)
        exercise_repo, history_repo = initialize_app()
        
        main_loop(history_repo, exercise_repo)
    except KeyboardInterrupt:
        print("\nZamykanie aplikacji Gymplaner...")
        sys.exit(0)

if __name__ == "__main__":
    main()