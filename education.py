class Education:
    def __init__(self):
        self.research_points = 0
        self.unlocked_content = []

    def add_research_points(self, points):
        self.research_points += points

    def unlock_content(self, content):
        if self.research_points >= content['cost']:
            self.research_points -= content['cost']
            self.unlocked_content.append(content)
        else:
            print("Not enough research points.")
