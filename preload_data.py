from habit_manager import HabitManager
from datetime import datetime, timedelta

def preload():
    manager = HabitManager()

    # Define habits
    habits_data = [
        {"name": "Read for 1 hour", "periodicity": "daily"},
        {"name": "Block social media for 8 hours", "periodicity": "daily"},
        {"name": "Practice math for 2 hours", "periodicity": "daily"},
        {"name": "Exercise", "periodicity": "weekly"},
        {"name": "Sunday Chores", "periodicity": "weekly"},
    ]

    # Create each habit
    for h in habits_data:
        manager.create_habit(h["name"], h["periodicity"])

    # Generate 4 weeks of dates
    today = datetime.now()

    # Add daily completions (28 days)
    for habit in manager.habits:
        if habit.periodicity == "daily":
            for i in range(28, 0, -1):
                date = today - timedelta(days=i)
                habit.completions.append(date.strftime("%Y-%m-%d"))

        elif habit.periodicity == "weekly":
            for i in range(4, 0, -1):
                date = today - timedelta(weeks=i)
                habit.completions.append(date.strftime("%Y-%m-%d"))

    # Save data
    manager.save_habits()
    print("Habits loaded successfully!")

preload()        