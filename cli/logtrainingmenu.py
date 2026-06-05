import datetime
import questionary
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table

from core.workoutsession import WorkoutSession
from core.exercises import WeightedExerciseLog, SetLoad
from cli.utils import parse_set_input, InvalidSetFormatError # zakładając, że to wydzielisz
from cli.exercisesmenu import add_exercise_ui

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
        choices.append(questionary.Choice(title="Add new exercise", value="NEW"))
        choices.append(questionary.Choice(title="End traning and go to summary", value="EXIT"))
        
        selected_exercise_id = questionary.select(
            "Choose your exercise:",
            choices=choices
        ).ask()
        
        if selected_exercise_id is None:
            console.print("[bold red]Action cancelled.[/]")
            break


        if selected_exercise_id == "EXIT":
            break
        elif selected_exercise_id == "NEW":
            add_exercise_ui(exercise_repo)
            continue
        
            
 
        exercise_log = WeightedExerciseLog(exercise_id=selected_exercise_id)
        
        last_performance = None
        last_date = None
    
        for past_session in reversed(workout_repo.workout_list):
            past_exercises = past_session.get("exercises", [])
            

            for past_ex in past_exercises:
                if past_ex.get("exercise_id") == selected_exercise_id:
                    last_performance = past_ex.get("sets", [])
                    last_date = past_session.get("date", "Unknown date")
                    break 
            
            if last_performance is not None:
                break 
                
   
        console.print("") 
        if last_performance:
            sets_formatted = ", ".join(f"{s['reps']}x{s['load']}kg" for s in last_performance)
            console.print(Panel(f"[bold yellow]{sets_formatted}[/]", title=f"Last time ({last_date})", expand=False))
        else:
            console.print("[dim italic]This is your first time doing this exercise. Good luck![/]")


        console.print("\n[dim]Enter your sets in the 'reps x load' format (e.g., 8x60). Type '0' to finish this exercise.[/]")
        set_number = 1
        
        while True:
            set_input = Prompt.ask(f"[light_sky_blue1]Set {set_number}[/]").strip()
            
            if set_input == "0":
                break
                
            try:
                reps, load = parse_set_input(set_input)
                exercise_log.add_set(SetLoad(reps=reps, load=load))
                set_number += 1
            except InvalidSetFormatError as e:
                console.print(f"[bold red]Error:[/] {e}")
                

        if exercise_log.sets_list:
            session.add_exercise_log(exercise_log)
            console.print(f"[bold green]Added {len(exercise_log.sets_list)} sets to your training.[/]\n")

    console.clear()
    workoutsummary(session,exercise_repo)
    
    if session.exercises_list:
        is_confirmed = Confirm.ask("\n[bold green]Are you sure you want to save this workout?[/]")
        if is_confirmed:
            session.complete_session()
            workout_repo.save_session(session)
            console.print("[bold green]Trening was saved![/]")
        else:
            console.print("[bold red]Cancelled[/]")
    else:
        console.print("[bold yellow]Your workout was empty, cancelled saving[/]")
        
    input("\nNaciśnij ENTER, to go back to menu...")



def workoutsummary(session, exercise_repo):
    console = Console()
    if not session.exercises_list:
        return
    table = Table(
        title=f"[bold cyan]WORKOUT SUMMARY | Date: {session.date}[/]",
        show_header=True, 
        header_style="bold magenta",
        expand=True
    )
    table.add_column("Exercise", min_width=20)
    table.add_column("Sets (Reps x Load)", justify="left")
    table.add_column("Max Load", justify="right", style="bold green")


    for exercise_log in session.exercises_list:
        exercise_id = exercise_log.exercise_id
        exercise_name = next(
            (exercise["name"] for exercise in exercise_repo.exercise_list if exercise["id"] == exercise_id), 
            "Unknown Exercise"
        )

        sets_formatted = ", ".join(f"{s.reps}x{s.load}kg" for s in exercise_log.sets_list)
        max_load = max([s.load for s in exercise_log.sets_list], default=0)
        table.add_row(
            f"[bold light_sky_blue1]{exercise_name}[/]",
            sets_formatted,
            f"{max_load} kg"
        )
    console.print(table)