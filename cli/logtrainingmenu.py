import datetime
import questionary
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

from core.workoutsession import WorkoutSession
from core.exercises import WeightedExerciseLog, SetLoad
from cli.utils import parse_set_input, InvalidSetFormatError # zakładając, że to wydzielisz

def logtrainingmenu(exercise_repo, workout_repo):
    
    
    
    
    session = WorkoutSession(date=datetime.date.today())
    
    while True:
        console = Console()
        console.clear()
        console.print(Panel.fit("[bold cyan]Fill working sets for your exercises.[/]", 
                            title="[bold green]TRAINING LOGGER[/]"))

        choices = [
            questionary.Choice(title=ex["name"], value=ex["id"]) 
            for ex in exercise_repo.exercise_list
        ]
        choices.append(questionary.Choice(title="[bold red]Zakończ i przejdź do podsumowania[/]", value="EXIT"))
        
        selected_exercise_id = questionary.select(
            "Wybierz ćwiczenie do wykonania:",
            choices=choices
        ).ask()
        
        if selected_exercise_id == "EXIT":
            break
            
        # Zaczynamy logować konkretne ćwiczenie
        exercise_log = WeightedExerciseLog(exercise_id=selected_exercise_id)
        
        console.print("\n[dim]Wpisz wyniki w formacie 'powtórzenia x ciężar' (np. 10x60). Wpisz '0', aby zakończyć to ćwiczenie.[/]")
        set_number = 1
        
        while True:
            set_input = Prompt.ask(f"[light_sky_blue1]Seria {set_number}[/]").strip()
            
            if set_input == "0":
                break
                
            try:
                # Tutaj nasz parser rzuci własny wyjątek, jeśli coś pójdzie nie tak
                reps, load = parse_set_input(set_input)
                exercise_log.add_set(SetLoad(reps=reps, load=load))
                set_number += 1
            except InvalidSetFormatError as e:
                console.print(f"[bold red]Błąd:[/] {e}")
                
        # Jeśli dodano jakiekolwiek serie, wrzucamy log do sesji
        if exercise_log.sets_list:
            session.add_exercise_log(exercise_log)
            console.print(f"[bold green]✔ Dodano {len(exercise_log.sets_list)} serii do treningu.[/]\n")

    # Podsumowanie i zapis
    console.clear()
    console.print(session)
    
    if session.exercises_list:
        is_confirmed = Confirm.ask("\n[bold green]Czy chcesz zapisać ten trening?[/]")
        if is_confirmed:
            session.complete_session()
            workout_repo.save_session(session)
            console.print("[bold green]Trening został pomyślnie zapisany![/]")
        else:
            console.print("[bold red]Trening odrzucony.[/]")
    else:
        console.print("[bold yellow]Sesja była pusta, anulowano zapis.[/]")
        
    input("\nNaciśnij ENTER, aby wrócić do menu...")