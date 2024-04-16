import os.path
import pygame
from sys import exit
from random import randint

scriptDir = os.path.dirname(os.path.abspath(__file__))

def menu(screen, menuFont, menuText, textColor):
    mainMenuBannerText = menuFont.render(menuText, True, textColor)
    screen.blit(mainMenuBannerText, (600, 220))

def main():
    # init()
    pygame.init()

    # setup the screen
    screen_width = 1400
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('The Swift and the Sulky')

    # setup the menu variables
    menuFont = pygame.font.SysFont("Modern", 40)
    textColor = (255, 255, 255)
    menuText = "Main Menu"

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    game_active = False

    startscreen = pygame.image.load(os.path.join(scriptDir,"car game graphics/","titlescreen.png")).convert_alpha()
    screen.blit(startscreen,(0,0))
    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_active:
            menu(screen, menuFont, menuText, textColor)

        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)

    # quit
    pygame.quit()

if __name__ == "__main__":
    main()
