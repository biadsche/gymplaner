from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm

from core.exerciserepo import ExerciseRepository
import time
from rich.progress import track

def exercisemenu(exercise_repo):
    while True:
        console = Console()
        console.clear()

        menu_options = """[green]1.[/] Add Exercise
[green]2.[/] Show saved Exercises
[green]3.[/] Search for an Exercise
[bold red]0.[/] Main Menu"""


        print(Panel.fit(menu_options,
                        title="[bold cyan] EXERCISE MENU [/]",
                        subtitle="Press number and press ENTER"))

        response = Prompt.ask(
                "[bold cyan]Choose option[/] [[green]1[/]/[green]2[/]/[green]3[/]/[bold red]0[/]]", 
                choices=["1", "2","3"],
                show_choices=False
            )

        if response == "1":
            add_exercise_ui(exercise_repo)
        elif response == "2":
            show_saved_exercises(exercise_repo)

        elif response == "0":
            break




def show_saved_exercises(exercise_repo):
    console = Console()
    console.clear()
#TODO do ulepszenia
    print("\n[bold cyan]--- SAVED EXERCISES ---[/]")
    for exercise in exercise_repo.exercise_list:
        name = exercise["name"]
        type = exercise["type"]
        muscles = ", ".join(exercise["target_muscles"]) 
        
        print(f"• [bold green]{name}[/] | Type: {type} | Muscles: {muscles}")
        
    input("\nEnter to go back to menu...")


def add_exercise_ui(exercise_repo):
    console = Console()
    console.clear()
    
    instruction = """[bold cyan]Fill all of the field below to add exercise to repository[/]"""
    console.print(Panel(instruction,
                title = "[light_sky_blue1]NEW EXERCISE CREATOR[n]"
          ))
    
    name = Prompt.ask("[royal_blue1]1. Enter name of your exercise: [/]").strip()
    if exercise_repo.get_exercise_by_name(name):
        print("[red3]This exercise already exists[/]")
        input("\n Press ENTER to go back...")
        return 
    
    exercise_type = Prompt.ask(
        "[light_sky_blue1]2. Type of your exercise[/]",
        choices=["1: Timed Exercise", "2: Weighted Exercise"]
    )

    note = Prompt.ask(
        "[light_sky_blue1]3. Note for the exercise [/] [dim](optional)[/]", 
        default="Empty Note"
    )

    console.print(f"\n[bold]Summary:[/] {name} | {exercise_type} | {note}")
    is_confirmed = Confirm.ask("[bold green] Are you sure you want to save this exercise?[/]")

    if is_confirmed:
        exercise_repo.add_exercise(name=name, exercise_type = exercise_type, target_muscles = [], note = note)
        for i in track(range(3), description="Processing..."):
            time.sleep(1)
        console.print("[bold green] Succes your exercise was added to your exercises")
    else:
        console.print("[bold red] Cancelled [/]")
    
    input("\n Press ENTER, to come back")