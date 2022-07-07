import sys, pygame

# Start the library
pygame.init()

# Set the screen's size of the game
size = width, height = 600, 600

# character's speed
SPEED = 5

# Start the game and set the screen
screen = pygame.display.set_mode(size)

# Get the character to draw
PLAYER_IMAGE = pygame.image.load("./assets/Jedikirby_2.gif")

# set a background image
bg = pygame.image.load("./assets/bk.jpeg")

# Function to draw in the window with the character
def draw_window(player, PLAYER):
    # Fill the screen and refresh the screen
    screen.fill((30, 30, 30))
    # Set the background
    screen.blit(bg, (0, 0))
    # Drax the character in screen
    screen.blit(PLAYER, (player.x, player.y))
    # Update the screen
    pygame.display.update()

# Game starts
def main():

    # Jump boolean to set if the player jump
    jump = False

    # Set shape for character
    PLAYER = pygame.transform.scale(PLAYER_IMAGE, (100, 100))

    # display character on screen
    # Position left, top, width, height
    top = 330
    left = 40
    player = pygame.Rect(left, top, 100, 100)

    run = True
    while run:
        # Set event to stop the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Detect character Movement if key is get_pressed
        keys_pressed = pygame.key.get_pressed()

        # Define movement on key pressed
        if keys_pressed[pygame.key.key_code("left")] and player.x > 0:
            # move the player to the left
            player.x -= 5
            # Turn the player to the left
            PLAYER = pygame.transform.flip(PLAYER_IMAGE, 1, 0)
        if keys_pressed[pygame.key.key_code("right")] and player.x < (width - 100):
            # move the player to the right
            player.x += 5
            # Turn the player to the right
            PLAYER = pygame.transform.flip(PLAYER_IMAGE, 0, 0)
        # Set a jump commande
        if keys_pressed[pygame.key.key_code("space")] and player.y > (top - 20):
            jump = True

        # Code to define jump behavior
        if jump:
            player.y -= 10
        elif not(jump) and player.y < top:
            player.y += 2
        if player.y < (top - 40):
            jump = False

        # Init draw for the game
        draw_window(player, PLAYER)

# Lauch the game
main()
