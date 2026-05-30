import pytest
from habit import Habit
from habit_manager import HabitManager
import analytics

def test_create_habit():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    assert len(manager.habits) == 1
    assert manager.habits[0].name == "Exercise" 

def test_mark_complete():
    habit = Habit("Exercise", "daily")
    habit.mark_complete()
    assert len(habit.completions) == 1

def test_get_streak():
    habit = Habit("Exercise", "daily")
    habit.completions = ["2026-05-17", "2026-05-18"]
    assert habit.get_streak() == 2

def test_list_all_habits():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.create_habit("Read", "weekly")
    result = analytics.list_all_habits(manager.habits)
    assert len(result) == 2

def test_filter_by_periodicity():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.create_habit("Chores", "weekly")
    result = analytics.filter_by_periodicity(manager.habits, "daily")
    assert len(result) == 1

def test_delete_habit():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.delete_habit("Exercise")
    assert len(manager.habits) == 0

def test_duplicate_habit():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.create_habit("Exercise", "daily")
    assert len(manager.habits) == 2

def test_weekly_streak():
    habit = Habit("Read", "weekly")
    habit.completions = ["2026-05-01", "2026-05-08", "2026-05-15"]
    assert habit.get_streak() == 3

def test_get_longest_streak_all():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.create_habit("Read", "weekly")
    manager.habits[0].completions = ["2026-05-17", "2026-05-18"]
    manager.habits[1].completions = ["2026-05-01", "2026-05-08", "2026-05-15"]
    result = analytics.get_longest_streak_all(manager.habits)
    assert result == 3

def test_get_longest_streak_one():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.habits[0].completions = ["2026-05-17", "2026-05-18"]
    result = analytics.get_longest_streak_one(manager.habits, "Exercise")
    assert result == 2

def test_get_status():
    habit = Habit("Exercise", "daily")
    habit.completions = ["2026-05-17", "2026-05-18"]
    status = habit.get_status()
    assert status["name"] == "Exercise"
    assert status["periodicity"] == "daily"
    assert status["total_completions"] == 2
    assert status["current_streak"] == 2

def test_save_and_load():
    manager = HabitManager()
    manager.create_habit("Exercise", "daily")
    manager.habits[0].completions = ["2026-05-17", "2026-05-18"]
    manager.save_habits()
    
    new_manager = HabitManager()
    new_manager.load_habits()
    assert len(new_manager.habits) == 1
    assert new_manager.habits[0].name == "Exercise"
    assert new_manager.habits[0].completions == ["2026-05-17", "2026-05-18"]

