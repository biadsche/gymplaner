from rich import print
from rich.panel import Panel

def menu():
    menu_options = """[green]1.[/] Log Traning
[green]2.[/] Add exercise 
[green]3.[/] Show history and progress
[bold red]0.[/] Exit"""
    

    print(Panel.fit(menu_options, 
                    title="[bold cyan]GYMPLANER - MAIN MENU[/]", 
                    subtitle="Press number and press ENTER",
                    padding=(0, 4)))
menu()