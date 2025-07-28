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
       "W  W   G       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      G    W  W",
       "W              W",
       "W         KK   D",
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

########## 1.7, 3.0, 3.3 ##########
# This function creates an actor object from the Actor class to represent the player & other objects
def SetupGame():
    global player # Define player as a global var that be accessed anywhere in your code
    global keysToCollect # A var to store all the keys the player needs to collect
    global gameOver
    player = Actor("player", anchor=("left", "top")) # Create a new Actor & set its anchor
    keysToCollect = []
    gameOver = False
    for y in range(GRID_HEIGHT): # Loop over each grid position
        for x in range(GRID_WIDTH):
            square = MAP[y][x] # Extracts the character from the MAP variable
            if square == "P": # Checks if the grid position is the player
                player.pos = GetScreenCoords(x, y) # Set the position of thr player
            elif square == "K":
                # Create an actor for that key
                key = Actor("key", anchor=("left", "top"))
                # Set the key's pos to this grid location
                key.pos = GetScreenCoords(x, y)
                # Add this key to our list of keys
                keysToCollect.append(key)
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

########## 1.8, 3.1 ##########
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
#########################

########## 3.1 ##########
def DrawGameOver():
    # Calculate and store the middle pos of the game screen
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    # Draw "Game Over" on the screen
    screen.draw.text("GAME OVER", midbottom = screenMiddle,
                     fontsize = GRID_SIZE, color="cyan", owidth=1)
#########################


# draw() is
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()
#########################

########## 2.2, 3.2 ##########
def MovePlayer(dx, dy):
    global gameOver
    if gameOver: # If the game is over
        # Stop the player from stopping the rest of the move function
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W": # If the player tries to move into a wall
        return # stop the function, don't let the player move
    elif square == "D":
        if len(keysToCollect) > 0: # If there are keys left to collect
            return # do not let the player exit the door if there are keys left
        else:
            gameOver = True # stop the function
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key) # Get grid posititon of the current key
        # Check if the new player pos matches the pos of one of the keys
        if x == keyX and y ==keyY:
            # Remove the key from the keys list
            keysToCollect.remove(key)
            break
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