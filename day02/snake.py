import pygame, random

# Initialize pygame
pygame.init()

# Set the display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = [WINDOW_WIDTH, WINDOW_HEIGHT]
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 20
Clock = pygame.time.Clock()
# Set game values
SNAKE_SIZE = 20
Head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0
# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 155, 10)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARKRED = (150, 0 , 0)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)
# I forgot what I was doing from here on out
# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED) #make a text object
title_rect = title_text.get_rect() # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) # places the box containing the text object's center to the middle of the screen.

#TODO: make a score_text object and assign a font render to it with text "Score: 0", antialias of True, color of GREEN, background color of DARKRED
score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
#TODO: make a score_rect object by assigning score_text.get_rect() to it.
score_rect = score_text.get_rect()
#TODO: place the topleft of score_rect to an x coordinate of 10 and y coordinate of 10
score_rect.topleft = (10, 10)

#TODO: make a game_over_text object and assign a font render to it with text "GAMEOVER", antialias of True, color of RED, background color of DARKRED
game_over_text = font.render("GAMEOVER", True, RED, DARKRED)
#TODO: make a game_over_rect object by assigning game_over_text.get_rect() to it.

game_over_rect = game_over_text.get_rect()
#TODO: place the center of game_over_rect to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
#TODO: make a continue_text  object and assign a font render to it with text "Press any key to play again", antialias of True, color of RED, background color of DARKGREEN
continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
#TODO: make a continue_rect  object by assigning continue_text.get_rect() to it.
continue_rect = continue_text.get_rect()
#TODO: place the center of continue_rect  to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT + 64
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)  # Correct
# Set sounds and music


# Set images (in this case, use simple rects...so just create their coordinates)

# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

# TODO: make a tuple for the head coordinates named head_coord and set to head_x, head_y, SNAKE_SIZE, SNAKE_SIZE
head_coord = (Head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
# TODO: make head_rect in a way similar to apple_rect, but with color GREEN instead.
Head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snake body by one position in the list

    # Update the x,y position of the snake head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
