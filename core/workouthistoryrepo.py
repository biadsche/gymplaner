import json
import os
from .workoutsession import WorkoutSession

#TODO przy pisaniu juz maina zhardcodowac sciezke
class WorkoutHistoryRepository:
    def __init__(self, file_path: str = "data/workoutrepo.json"):
        self.file_path = file_path
        self.workout_list = []
        self.file_exists_check()
        self.load_database()
        
        
    def load_database(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as repo_file:
                self.workout_list = json.load(repo_file)
        except json.decoder.JSONDecodeError:
            print("Corrupted file or the file is empty")
            self.workout_list = []
            
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
        
    def save_session(self, session: WorkoutSession):
        session_dict = session.to_dict()
        self.workout_list.append(session_dict)
        
        with open(self.file_path, 'w', encoding='utf-8') as repo_file:
            json.dump(self.workout_list, repo_file, indent=4, ensure_ascii=False)
            
    def get_last_performance(self, exercise_id : str) -> dict | None:
        last_performance_dict = {}
        for workout_session in reversed(self.workout_list):
            for exercise in workout_session["exercises"]:
                if exercise.get("exercise_id") == exercise_id:
                    set_number = 0
                    for set_data in exercise["sets"]:
                        last_performance_dict[set_number] = {
                            "reps": set_data["reps"],
                            "load": set_data["load"]
                        }
                        set_number +=1
                    return last_performance_dict
        return None
                         
                         
    def get_every_performance(self,exercise_id : str) -> list:
        performance_history = []
        for workout_session in reversed(self.workout_list):
            for exercise in workout_session["exercises"]:
                if exercise.get("exercise_id") == exercise_id:
                    set_number = 0
                    session_performance = {}
                    
                    for set_data in exercise["sets"]:
                        session_performance[set_number] = {
                            "reps": set_data["reps"],
                            "load": set_data["load"]
                        }
                        set_number +=1
                    date = workout_session.get("date", "Unknown Date")
                    session_id = workout_session.get("session_id")
                        
                    performance_history.append({
                        "session_id" : session_id,
                        "date": date,
                        "sets": session_performance
                    })
                        
        return performance_history


