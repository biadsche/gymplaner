import json
import os
from .exercises import MuscleGroup

class ExerciseRepository:
    def __init__(self, file_path: str = "gymplaner/data/exercisesrepo.json"):
        self.file_path = file_path
        self.file_exists_check()
    
    def file_exists_check(self):
        if os.path.exists(self.file_path):
            return True
        else:
            with open(self.file_path, 'w') as fp:
                json.dump([], fp)
            return False
    
    
    def add_exercise(self, name: str, exercise_type: str, target_muscles: list[MuscleGroup] = None, note: str = ""):
        with open(self.file_path, 'r', encoding='utf-8') as repo_file:
            saved_exercises = json.load(repo_file)
        
        #bool to check if file already exists
        already_exists = False
        for exercise in saved_exercises:
            if exercise["name"].lower() == name.lower():
                already_exists = True
        
        if already_exists:
            return False
        
        muscles_list = [muscle.value for muscle in target_muscles] if target_muscles else []

        new_exercise = {
            "name": name,
            "type": exercise_type,
            "target_muscles" : muscles_list,
            "note" : note
        }

        saved_exercises.append(new_exercise)
        updated_list = json.dumps(saved_exercises, indent=4, ensure_ascii=False)
        with open(self.file_path, 'w') as repo_file:
            repo_file.write(updated_list)

        return True
    
    def get_exercise_by_name(self, name:str) -> dict | None:
        with open(self.file_path, 'r', encoding='utf-8') as repo_file:
            saved_exercises = json.load(repo_file) 

        for exercise in saved_exercises:
            if exercise["name"].lower() == name.lower():
                return exercise

        return None
    
#TODO Wypisanie wszystkich cwiczen z danej grupy miesniowej itd
    def get_exercise_by_muscle(self, searching_target_muscle: str) -> list[dict] | None:
        with open(self.file_path, 'r', encoding='utf-8') as repo_file:
            saved_exercises = json.load(repo_file)
        
        matching_exercises = []

        for exercise in saved_exercises:        
            for target_muscle in exercise["target_muscles"]:
                if searching_target_muscle in exercise.get("target_muscles", []):
                    matching_exercises.append(exercise)
        
        return matching_exercises



#TODO kiedys implementacja raga do lepszego wyszukiwania cwiczen
