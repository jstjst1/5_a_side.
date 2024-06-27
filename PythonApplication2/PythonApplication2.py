import random

# Define the Player class to represent an outfield player with specific attributes
class Player:
    def __init__(self, name, dribbling, shooting, passing, defending):
        self.name = name
        self.dribbling = dribbling
        self.shooting = shooting
        self.passing = passing
        self.defending = defending

    # Method to edit the player's attributes interactively with prompts
    def edit_attributes(self):
        while True:
            print(f"\nEditing {self.name}'s attributes:")
            print(f"1. Name: {self.name}")
            print(f"2. Dribbling: {self.dribbling}")
            print(f"3. Shooting: {self.shooting}")
            print(f"4. Passing: {self.passing}")
            print(f"5. Defending: {self.defending}")
            choice = input("Select an attribute to edit (1-5) or 'q' to quit: ").strip()
            if choice == '1':
                self.name = input("Enter new name: ").strip()
            elif choice == '2':
                self.dribbling = int(input("Enter new dribbling rating (0-100): "))
            elif choice == '3':
                self.shooting = int(input("Enter new shooting rating (0-100): "))
            elif choice == '4':
                self.passing = int(input("Enter new passing rating (0-100): "))
            elif choice == '5':
                self.defending = int(input("Enter new defending rating (0-100): "))
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please try again.")

# Define the Goalkeeper class to represent a Goalkeeper with specific attributes
class Goalkeeper:
    def __init__(self, name, shot_stopping, catching):
        self.name = name
        self.shot_stopping = shot_stopping
        self.catching = catching

    # Method to edit the Goalkeeper's attributes interactively with prompts
    def edit_attributes(self):
        while True:
            print(f"\nEditing {self.name}'s attributes:")
            print(f"1. Name: {self.name}")
            print(f"2. Shot Stopping: {self.shot_stopping}")
            print(f"3. Catching: {self.catching}")
            choice = input("Select an attribute to edit (1-3) or 'q' to quit: ").strip()
            if choice == '1':
                self.name = input("Enter new name: ").strip()
            elif choice == '2':
                self.shot_stopping = int(input("Enter new shot stopping rating (0-100): "))
            elif choice == '3':
                self.catching = int(input("Enter new catching rating (0-100): "))
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please try again.")

# Define the Team class to represent a team consisting of outfield players and a Goalkeeper
class Team:
    def __init__(self):
        self.outfield_players = []
        self.goalkeeper = None

    # Method to add an outfield player to the team
    def add_outfield_player(self, player):
        self.outfield_players.append(player)

    # Method to set the Goalkeeper for the team
    def set_goalkeeper(self, goalkeeper):
        self.goalkeeper = goalkeeper

    # Method to calculate the total team strength based on player attributes
    def team_strength(self):
        outfield_strength = sum(p.dribbling + p.shooting + p.passing + p.defending for p in self.outfield_players)
        goalkeeper_strength = self.goalkeeper.shot_stopping + self.goalkeeper.catching
        return outfield_strength + goalkeeper_strength

# Function to input player data from the user
def input_player_data(team_number):
    outfield_players = []
    print(f"\nEnter player data for Team {team_number}")
    for i in range(4):
        name = input(f"Enter name for outfield player {i+1}: ")
        dribbling = int(input(f"Enter dribbling rating for {name} (0-100): "))
        shooting = int(input(f"Enter shooting rating for {name} (0-100): "))
        passing = int(input(f"Enter passing rating for {name} (0-100): "))
        defending = int(input(f"Enter defending rating for {name} (0-100): "))
        player = Player(name, dribbling, shooting, passing, defending)
        outfield_players.append(player)

    goalkeeper_name = input("Enter name for the goalkeeper: ")
    shot_stopping = int(input(f"Enter shot stopping rating for {goalkeeper_name} (0-100): "))
    catching = int(input(f"Enter catching rating for {goalkeeper_name} (0-100): "))
    goalkeeper = Goalkeeper(goalkeeper_name, shot_stopping, catching)

    return outfield_players, goalkeeper

# Function to simulate the match based on team strengths and random factors
def simulate_match(team1, team2):
    team1_strength = team1.team_strength()
    team2_strength = team2.team_strength()

    # Randomly determine initial goals scored by each team
    team1_goals = random.randint(0, 5)
    team2_goals = random.randint(0, 5)

    # Calculate advantages based on team strengths and randomness
    team1_advantage = random.random() + team1_strength / (team1_strength + team2_strength)
    team2_advantage = random.random() + team2_strength / (team1_strength + team2_strength)

    # Adjust goals based on calculated advantages
    if team1_advantage > team2_advantage:
        team1_goals += 1
    elif team2_advantage > team1_advantage:
        team2_goals += 1

    # Display match result
    print(f"\nMatch Result: Team 1 {team1_goals} - {team2_goals} Team 2")

# Function to edit a team's players and goalkeeper
def edit_team(team):
    while True:
        print("\nEditing team:")
        for i, player in enumerate(team.outfield_players):
            print(f"{i + 1}. {player.name}")
        print(f"{len(team.outfield_players) + 1}. {team.goalkeeper.name} (Goalkeeper)")

        choice = input("Select a player to edit (1-5) or 'q' to quit: ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < 4:
                team.outfield_players[index].edit_attributes()
            elif index == 4:
                team.goalkeeper.edit_attributes()
            else:
                print("Invalid choice. Please try again.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to run the simulation
def main():
    # Store teams to retain their states
    team1 = Team()
    team2 = Team()

    while True:
        # Input player data for both teams
        if not team1.outfield_players or not team1.goalkeeper:
            team1_outfield_players, team1_goalkeeper = input_player_data(1)
            for player in team1_outfield_players:
                team1.add_outfield_player(player)
            team1.set_goalkeeper(team1_goalkeeper)

        if not team2.outfield_players or not team2.goalkeeper:
            team2_outfield_players, team2_goalkeeper = input_player_data(2)
            for player in team2_outfield_players:
                team2.add_outfield_player(player)
            team2.set_goalkeeper(team2_goalkeeper)

        # Simulate the match
        simulate_match(team1, team2)

        # Ask the user what they want to do next
        print("\nWhat would you like to do next?")
        print("1. Edit player attributes")
        print("2. Rerun the simulation with the current settings")
        print("3. Exit")
        next_action = input("Enter the number of your choice: ").strip()

        if next_action == '1':
            while True:
                team_choice = input("\nWhich team do you want to edit? (1 or 2, 'q' to quit editing): ").strip()
                if team_choice == '1':
                    edit_team(team1)
                elif team_choice == '2':
                    edit_team(team2)
                elif team_choice.lower() == 'q':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif next_action == '2':
            continue
        elif next_action == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()