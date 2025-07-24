########## 1.3 ##########
import pgzrun # imports the pgzrun module

# Define width and height of the game grid & size  of each grid tile
GRID_WIDTH = 16 # defines How many squares wide the game board is
GRID_HEIGHT = 12 # defines How many squares tall the game board is
GRID_SIZE = 50 # Each tile is 50 by 50 pixels

# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
#########################

########## 1.5 ##########
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]
#########################

########## 1.4 ##########
# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# This function converts a grid position to screen coordinates
def DrawBackground():
    for y in range (GRID_HEIGHT): # loop over each grid row
        for x in range (GRID_WIDTH): # loop over each grid column
            screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named imaged at the given screen position
#########################

########## 2.1 ##########
# This function takes in an actor as an argument &
# returns the position of the actor on the grid
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
#########################

########## 1.7 ##########
# This function creates an actor object from the Actor class to represent the player
def SetupGame():
    global player # Define player as a global var that be accessed anywhere in your code
    player = Actor("player", anchor=("left", "top")) # Create a new Actor & set its anchor
    for y in range(GRID_HEIGHT): # Loop over each grid position
        for x in range(GRID_WIDTH):
            square = MAP[y][x] # Extracts the character from the MAP variable
            if square == "P": # Checks if the grid position is the player
                player.pos = GetScreenCoords(x, y) # Set the position of thr player
#########################

########## 1.6 ##########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

########## 1.8 ##########
def DrawActors():
    player.draw()
#########################

# draw() is
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
#########################

########## 2.2 ##########
def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x, y)
#########################

########## 2.3 ##########
# This Function gets a key from the user and moves the player based on the input
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0) # Player moves left one on the grid
    elif key == keys.UP:
        MovePlayer(0, -1) # Playe moves up one on the grid
    elif key == keys.RIGHT:
        MovePlayer(1, 0) # Player moves right one on the grid
    elif key == keys.DOWN:
        MovePlayer(0, 1) # Player moves down one on the grid
#########################



# Start the Pygame
SetupGame()
pgzrun.go()