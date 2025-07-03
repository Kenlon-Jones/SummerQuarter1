# Build a RPS game
# 2-players
# Each player picks between rock, paper and scissors
# Each player's choice is compared:
# Rock > Scissors
# Scissors > paper
# Paper > Rock

# 0. Prompt the players for their names
# 1. Prompt player 1 for RPS
# 2. Promp player 2 for RPS
# 3. Compare p1 and p2 choies and decide a winner

def RPS():
    print("Welcome to Rock Paper Scissors!")

    # Gather Player namers
    player1 = input("Player 1, Please enter your name: ")
    player2 = input("Player 2, Please enter your name: ")

    # Gather Player moves
    p1_Choice = input(f"{player1}, choose between Rock, Paper, & Scissors: ")

    while not IsValidMove(p1_Choice):
        print("Invalid Move! Please try again")
        p1_Choice = input(f"{player1}, choose between Rock, Paper, & Scissors: ")

    p2_Choice = input(f"{player2}, choose between Rock, Paper, & Scissors: ")
    
    while not IsValidMove(p2_Choice):
        print("Invalid Move! Please try again")
        p2_Choice = input(f"{player2}, choose between Rock, Paper, & Scissors: ")

    # Compare Player moves
    if p1_Choice == p2_Choice:
        print("It's a draw!")

    elif p1_Choice == "rock" and p2_Choice == "scissors": 
        print(f"Rock beats scissors, {player1} wins!")

    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"Paper beats rock, {player1} wins!")

    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"Scissors beats paper, {player1} wins!")

    elif p2_Choice == "rock" and p1_Choice == "scissors": 
        print(f"Rock beats scissors, {player2} wins!")

    elif p2_Choice == "paper" and p1_Choice == "rock":
        print(f"Paper beats rock, {player2} wins!")

    elif p2_Choice == "scissors" and p1_Choice == "paper":
        print(f"Scissors beats paper, {player2} wins!")


def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]

    if playerMove.lower() in validMoves: 
        return True
    else:
        return False

RPS()