import json
from habit import Habit
class HabitManager:
    def __init__(self):
        self.habits = [] # this is a list [] can add/remove habits unlike a tuple()
        self.file_path = "habits.json"

    def create_habit(self, name, periodicity):
        """Creates a new Habit object with the given name and periodicity, adds it to
        the habits list, and saves to the JSON file."""
        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)
        print("habit successfully created")
        self.save_habits() # always end with parentheses when calling a method

    def delete_habit(self, name):
        """Finds habit by name, removes it, and saves to JSON"""
        for habit in self.habits:
            if habit.name == name:
                self.habits.remove(habit)
                print("habit deleted successfully")
                self.save_habits()

    def save_habits(self):
        """Converts habits to dictionaries, writes to JSON"""
        data = {
        "habits": [
        {
               "name": habit.name,
               "periodicity": habit.periodicity,
               "created_at": habit.created_at,
               "completions": habit.completions    
                    
        }
        for habit in self.habits

    ]
}
        with open(self.file_path, "w") as f:
            json.dump(data, f)
 
    def load_habits(self):
        """Reads JSON file, converts back to Habit objects"""
        try:
            with open(self.file_path, "r") as f:
               data = json.load(f)
               for h in data["habits"]:
                   habit = Habit(h["name"], h["periodicity"])
                   habit.created_at = h["created_at"]
                   habit.completions = h["completions"]
                   self.habits.append(habit)
        except FileNotFoundError:
            pass
                            



                