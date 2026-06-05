import datetime
import questionary
from rich.console import Console
from rich.prompt import Prompt, Confirm

from core.workoutsession import WorkoutSession
from core.exercises import WeightedExerciseLog, SetLoad
from cli.utils import parse_set_input, InvalidSetFormatError

def logtrainingmenu(exercise_repo, workout_repo):
    while True:
        console = Console()
        console.clear()