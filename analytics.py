from habit import Habit
def list_all_habits(habits):
    return habits


def filter_by_periodicity(habits, periodicity):
    return [habit for habit in habits if habit.periodicity == periodicity]

def get_longest_streak_all(habits):
    if not habits:
        return 0
    return max(habits, key=lambda habit: habit.get_streak()).get_streak()

def get_longest_streak_one(habits, name):
    for habit in habits:
        if habit.name == name:
            return habit.get_streak()
    return 0
