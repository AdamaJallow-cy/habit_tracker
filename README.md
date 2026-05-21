# Habit Tracking App
The Habit Tracker is a Python application designed to help users build and maintain good habits. Users can create habits, mark them as completed, and track their progress over time using streaks and simple analytics.

This project was developed with Object-Oriented and Functional Programming in Python as a hands-on way to practice OOFP concepts such as classes, objects, encapsulation, and modular design in a real application.

The system is organized into separate classes for managing habits, handling analytics, and interacting with the user through a command line interface (CLI). This helps keep the program structured, readable, and easier to improve in the future.  

## Features
- Create, delete and complete habits
- Track habit streaks and progress
- Analyse and retrieve habit data
- Support for daily and weekly habits periods
- Persistent data storage using JSON
- Predefined habits with 4 weeks of sample data
- Command line interface for user interaction 
- Unit testing implemented with pytest

## Project Structure

```
habit_tracker/
│   analytics.py        → Functional analytics module
│   habit.py            → Habit class definition
│   habit_manager.py    → Manages all habit operations
│   main.py             → CLI interface and main loop
│   preload_data.py     → Loads predefined habits with sample data
│   test_habits.py      → Unit tests using pytest
│   habits.json         → Persistent data storage
│   README.md           → Project documentation

```

## Requirements

- Python 3.7 or later
- pytest (for running tests)

Install pytest using:

```bash
pip install pytest
```


## Installation

1. Prerequisites
  - Git installed on your machine
  - Download and install Python 3.7 or later from https://www.python.org

2. Clone the repository: Open Git and execute the    following command:

```bash
git clone https://github.com/AdamaJallow/habit_tracker.git
```

3. Navigate into the project folder:

```bash
cd habit_tracker
```

4. Load predefined habits:

```bash
python preload_data.py
```

## How to Run
- To start the application, Open a command line interface(CLI) and run the following command:

```bash
python main.py
```

## How to Use

| Option | Description |
|--------|-------------|
| 1 | Create a new habit |
| 2 | Delete a habit |
| 3 | Complete a habit |
| 4 | View all habits |
| 5 | View habits by periodicity |
| 6 | View longest streak |
| 7 | Exit |

## How to Run Tests

```bash
python -m pytest test_habits.py -v
```

## Predefined Habits

The app comes with 5 predefined habits and 4 weeks of 
sample data for testing purposes. Run the following 
command to load them:

```bash
python preload_data.py
```

| Habit | Periodicity |
|-------|-------------|
| Read for 1 hour | Daily |
| Block social media for 8 hours | Daily |
| Practice math for 2 hours | Daily |
| Exercise | Weekly |
| Sunday Chores | Weekly |


