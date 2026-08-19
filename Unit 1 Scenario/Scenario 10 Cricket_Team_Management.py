class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

    def categorize(self):  
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 200:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.player_name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.categorize())
        print()


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all_players(self):
        print("----- Cricket Team -----")
        for player in self.players:
            player.display()


p1 = Player("Virat", 18, 750)
p2 = Player("Rohit", 45, 450)
p3 = Player("Rahul", 1, 150)

team = Team()

team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.display_all_players()

"""
----- Cricket Team -----
Player Name: Virat
Jersey Number: 18
Runs: 750
Category: Excellent

Player Name: Rohit
Jersey Number: 45
Runs: 450
Category: Good

Player Name: Rahul
Jersey Number: 1
Runs: 150
Category: Average
"""