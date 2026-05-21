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