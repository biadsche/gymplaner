from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console

from .exercisesmenu import exercisemenu
from cli.logtrainingmenu import logtrainingmenu

def menu(exercise_repo, workout_repo):
    while True:
        console = Console()
        console.clear()
        menu_options = """[green]1.[/] Log Traning
[green]2.[/] Exercises
[green]3.[/] Workouts
[bold red]0.[/] Exit"""
    

        print(Panel.fit(menu_options, 
                        title="[bold cyan]GYMPLANER - MAIN MENU[/]", 
                        subtitle="Choose a number and press ENTER",
                        padding=(0,12)))
        

        response = Prompt.ask(
            "[bold cyan]Choose option[/] [[green]1[/]/[green]2[/]/[green]3[/]/[bold red]0[/]]", 
            choices=["1", "2", "3", "0"],
            show_choices=False
        )

        if response == "0":
            break
        elif response == "1":
            console.clear()
            logtrainingmenu(exercise_repo,workout_repo)   
        elif response == "2":
            console.clear()
            exercisemenu(exercise_repo)





