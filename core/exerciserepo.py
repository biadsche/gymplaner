import json
import os
from .exercises import MuscleGroup
import uuid


class ExerciseRepository:
    def __init__(self, file_path: str = "data/exercisesrepo.json"):
        self.file_path = file_path
        self.exercise_list = []
        self.file_exists_check()
        self.load_database()
    
    def file_exists_check(self):
        dir_name = os.path.dirname(self.file_path)
        if dir_name and not os.path.isdir(dir_name):
            os.makedirs(dir_name, exist_ok=True)
        if os.path.exists(self.file_path):
            return True
        else:
            with open(self.file_path, 'w') as fp:
                json.dump([], fp)
            return False
    
    def load_database(self):
        with open(self.file_path, 'r', encoding='utf-8') as repo_file:
            self.exercise_list = json.load(repo_file)
    
    
    def add_exercise(self, name: str, exercise_type: str, target_muscles: list[MuscleGroup] = None, note: str = ""):
        
        #sprawdzam czy cwiczenie juz istnieje
        for exercise in self.exercise_list:
            if exercise["name"].lower() == name.lower():
                return None
        #TODO tu mozna to tak przepisac zeby uzyc metody to_dict
                    
        new_exercise_id = str(uuid.uuid4())
        muscles_list = [muscle.value for muscle in target_muscles] if target_muscles else []
        new_exercise = {
            "id": new_exercise_id,
            "name": name,
            "type": exercise_type,
            "target_muscles": muscles_list,
            "note": note
        } 
        
        self.exercise_list.append(new_exercise)
        
        with open(self.file_path, 'w', encoding='utf-8') as repo_file:
            json.dump(self.exercise_list, repo_file, indent=4, ensure_ascii=False)
            
        return new_exercise_id
    
    def get_exercise_by_name(self, name:str) -> dict | None:
        for exercise in self.exercise_list:
            if exercise["name"].lower() == name.lower():
                return exercise

        return None
    

    def get_exercise_by_muscle(self, searching_target_muscle: str) -> list[dict]:

        matching_exercises = []
        
        for exercise in self.exercise_list:        
            for target_muscle in exercise["target_muscles"]:
                if searching_target_muscle in exercise.get("target_muscles", []):
                    matching_exercises.append(exercise)
                    break
        
        return matching_exercises


    def remove_exercise(self, exercise_id: str):
        self.exercise_list = [ex for ex in self.exercise_list if ex["id"] != exercise_id]
        with open(self.file_path, 'w', encoding='utf-8') as repo_file:
                json.dump(self.exercise_list, repo_file, indent=4, ensure_ascii=False)

#TODO kiedys implementacja raga do lepszego wyszukiwania cwiczen
