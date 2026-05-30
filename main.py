from habit_manager import HabitManager
import analytics
def main():
    manager = HabitManager()
    manager.load_habits()

    while True:
        print("\n== Habit Tracker ===")
        print("1. Create a habit")
        print("2. Delete a habit")
        print("3. Complete a habit")
        print("4. View all habits")
        print("5. View habits by periodicity")
        print("6. View longest streak")
        print("7. Exit")

        choice = input("\nEnter your pick: ")
        if choice == "1":
            while True:
                name = input("Enter habit name: ").strip()
                if name:
                    break
                else:
                    print("Habit name cannot be empty. Please enter a valid name.") 
            while True:
                 periodicity = input("Enter periodicity (daily/weekly): ").lower()
                 if periodicity in ["daily", "weekly"]:
                     break
                 else:
                     print("Invalid periodicity. Please enter 'daily' or 'weekly'.")
            manager.create_habit(name, periodicity)

        elif choice == "2":
            while True:
              name = input("Enter the habit you want to delete: ").strip()
              if name:
                  break
              else:
                  print("Habit name cannot be empty. Please enter a valid name.")
            manager.delete_habit(name)

        elif choice == "3":
            while True:
                name = input("Enter completed habit: ").strip()
                if name:
                    break
                else:
                    print("Habit name cannot be empty. Please enter a valid name.")
            for habit in manager.habits:
                if habit.name == name:
                    habit.mark_complete()
                    manager.save_habits()
                    break
                
        elif choice == "4":
            habits = analytics.list_all_habits(manager.habits)
            for habit in habits:
                print(habit)
            input("\nPress Enter to continue...")    
            
        elif choice == "5":
            while True:
                 periodicity = input("Enter periodicity (daily/weekly): ").lower()
                 if periodicity in ["daily", "weekly"]:
                     break
                 else:
                     print("Invalid periodicity. Please enter 'daily' or 'weekly'.")   
            habits = analytics.filter_by_periodicity(manager.habits, periodicity)
            for habit in habits:
                print(habit.name)

        elif choice == "6":
            streak = analytics.get_longest_streak_all(manager.habits)
            print(f"highest streak: {streak}")
            input("\nPress Enter to continue...")
        elif choice == "7":
            break
        else:
            print("invalid choice, please try again")

if __name__ == "__main__":
    main()

