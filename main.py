#TODO funckjonalnosc zapiyswania treningow na telefonie
#TODO dodac funkcjonalnosc jakiegos goala
#TODO funkcjonalnosc agenta do jakiegos planowania albo cos
#TODO mozliwosc resetowania goali

from core.exerciserepo import ExerciseRepository
from cli.menu import menu

def main():
    repo = ExerciseRepository()
    menu(repo)



if __name__ == "__main__":
    main()