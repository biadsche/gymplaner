from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console

from exercisesmenu import exercisemenu

def menu():
    while True:
        console = Console()
        console.clear()

        menu_options = """[green]1.[/] Log Traning
[green]2.[/] Exercises
[green]4.[/] Workouts
[green]4.[/] Splits 
[green]5.[/] History and progress
[bold red]0.[/] Exit"""
    

        print(Panel.fit(menu_options, 
                        title="[bold cyan]GYMPLANER - MAIN MENU[/]", 
                        subtitle="Press number and press ENTER"))



        response = Prompt.ask(
            "[bold cyan]Choose option[/] [[green]1[/]/[green]2[/]/[green]3[/]/[bold red]0[/]]", 
            choices=["1", "2", "3", "0"],
            show_choices=False
        )

        if response == "0":
            break
        if response == "1":
            console.clear()
            exercisemenu()





