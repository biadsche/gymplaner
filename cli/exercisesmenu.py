from rich import print
from rich.panel import Panel
from rich.prompt import Prompt



def exercisemenu():

    menu_options = """[green]1.[/] Add Exercise
[green]2.[/] Show saved Exercises
[bold red]0.[/] Main Menu"""


    print(Panel.fit(menu_options,
                    title="[bold cyan] EXERCISE MENU [/]",
                    subtitle="Press number and press ENTER"))

    response = Prompt.ask(
            "[bold cyan]Choose option[/] [[green]1[/]/[green]2[/]/[green]3[/]/[bold red]0[/]]", 
            choices=["1", "2","0"],
            show_choices=False
        )



