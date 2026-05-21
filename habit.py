from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now().strftime("%Y-%m-%d")
        self.completions = []

    def mark_complete(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.completions:
            self.completions.append(today)
            print(f"Habit '{self.name}' done for today")
        else:
            print(f"Habit '{self.name}' already done")

    def get_streak(self):
        if not self.completions:
            return 0
        streak = 1
        sorted_dates = sorted(self.completions)
        for i in range(len(sorted_dates) - 1, 0, -1):
            date1 = datetime.strptime(sorted_dates[i], "%Y-%m-%d")
            date2 = datetime.strptime(sorted_dates[i-1], "%Y-%m-%d")
            diff = (date1 - date2).days
            if self.periodicity == "daily" and diff == 1:
                streak += 1
            elif self.periodicity == "weekly" and diff <= 7:
                streak += 1
            else:
                break
        return streak

    def get_status(self):
        status = {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "total_completions": len(self.completions),
            "current_streak": self.get_streak()
        }
        return status
    def __str__(self):
        return (f"Habit: {self.name} | "
                f"Periodicity: {self.periodicity} | "
                f"Streak: {self.get_streak()} days")
    def __repr__(self):
        return (f"Habit(name='{self.name}', "
                f"periodicity='{self.periodicity}')")
        
    
    