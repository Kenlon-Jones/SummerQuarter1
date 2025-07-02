# This program will allocate teams randomly from a list of names
# 1. Import the random module
# 2. Create a list of every Genius
# 3. Use the random module to randomly shuffle the list
# 4. Loop Through the list and display each team's players
# 5. using an if statement to see if the user is happy with the teams
# If not, it will shuffle again. If so, the program terminates

import random # Import the random module 

# Create a list of players stored in the player variable
players = ["Kamari", "Max", "Braylen",
           "Jeffrey", "Xaiver", "Avery",
           "Carl", "Walter", "Darren",
           "EJ", "Nahum", "Joaquin",
           "Marshawn", "Ja'Den", "Isaiah",
           "Kenlon", "Nishad", "Kauri",
           "Kriss", "Joseph", "Semaj",
           "Tay", "Taqari", "Jarmauri"]

def PickTeams(players):     # Create our function
    random.shuffle(players) # Shuffle the list of players
    team1 = players[:len(players) // 2] # Put the 1st half of the players into the 1st team
    teamCaptain1 = team1[random.randrange(0, 12)] # Ramdomy assign a team captain

    print("TEAM 1")
    print("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)

    team2 = players[len(players) // 2:] # Put the 2nd half of the players in the second team
    teamCaptain2 = team2[random.randrange(0, 12)]

    print("TEAM 2")
    print("Team 2 Captain: " + teamCaptain2)
    for player in team2:
        print(player)

PickTeams(players)