class Resources:
    def __init__(self):
        self.time = 12 * 7  # hours per week
        self.dollars = 1000  # starting money
        self.psyche = 100  # starting psyche value
        self.status = 1  # initial status

    def update_resources(self, labor_hours, research_hours, leisure_hours):
        self.dollars += labor_hours * self.calculate_labor_income()
        self.psyche += leisure_hours * self.calculate_psyche_boost()
        self.update_status()

    def calculate_labor_income(self):
        return 10

    def calculate_psyche_boost(self):
        return 1

    def update_status(self):
        if self.dollars < 500:
            self.status -= 1
        elif self.dollars > 2000:
            self.status += 1
        if self.psyche <= 0:
            self.psyche = 0
            print("Game Over: Psyche depleted.")
