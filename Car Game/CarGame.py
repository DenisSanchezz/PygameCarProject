import pygame
import sys
import os.path
from random import randint
scriptDir = os.path.dirname(os.path.abspath(__file__))

def menu(screen, menuFont, buttons, menuActive):
    #bg
    #screen.fill('0x737373')
    
    startscreen = pygame.image.load(os.path.join(scriptDir,"Graphics/","titlescreen.png")).convert_alpha()
    screen.blit(startscreen,(0,0))

    #mainMenuBannerText = menuFont.render(menuText, True, ('0x000000'))
    #screen.blit(mainMenuBannerText, (150, 60))

    for text, color, rect in buttons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, ('0x000000'))
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
def title(screen, TitleFont, TitleText, white):
    mainText = TitleFont.render(TitleText, True, white)
    screen.blit(mainText, (250, 100))

def credits(screen, menuFont, white, black, creditsActive, creditsButtons):
    screen.fill(black)
    
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)

    #   PUT CREDITS HERE
    creditsText = menuFont.render("",                                  
                                    True, white)

    screen.blit(creditsText, (450, 150))
    screen.blit(backButtonText, backButtonTextRect)

    creditsActive = True
    pygame.display.update()

    while creditsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.collidepoint(event.pos):
                        creditsActive = False
        print("Credits is actives")

def skins(screen, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, playerSurface, playerRect):
    screen.fill(black)
    
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)
    screen.blit(backButtonText, backButtonTextRect)
    
    for text, color, rect in skinsButtons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, white)
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
    skinsActive = True
    
    pygame.display.update()
    while skinsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for text, color, rect in creditsButtons:
                        if rect.collidepoint(event.pos):
                            if text == "RED":
                                print("clicked red button")
                                #play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                #skinsActive = False
                            elif text == "GREEN":
                                print("clicked green button")
                                #play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                #skinsActive = False
                            elif text == "BLUE":
                                print("clicked blue button")
                                #play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                #skinsActive = False
                    if backButton.collidepoint(event.pos):
                        #change so it goes to the level screen 
                        main()
                        menuActive = True
                        skinsActive = False
        print("Skins is active")

def play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect):
    #fill screen to remove the menu stuff
    screen.fill(black)

    screen.blit(roadSurface, roadSurfaceRect)
    screen.blit(playerSurface, playerRect)

    while gameActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        print("gameActive")

def main():
    # Setup
    pygame.init()

    # setup the screen
    screenWidth = 1000
    screenHeight = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('The Swift and the Sulky')

    # setup the menu variables
    menuFont = pygame.font.SysFont("Consolas", 40, bold=True)
    menuText = "Main Menu"
    white = '0xFFFFFF'
    black = '0x000000'

    titleFont = pygame.font.SysFont("Consolas", 40)
    titleText = "The Swift and the Sulky"

    # list to store all the buttons text, color, and position
    buttons = [
        ("PLAY", ('0x00FF00'), pygame.Rect(350, 225, 300, 75)),
        ("CREDITS", ('0xFFFF00'), pygame.Rect(350, 325, 300, 75)),
        ("QUIT", ('0xFF0000'), pygame.Rect(350, 425, 300, 75))
    ]

    # buttons used in the credits screen
    creditsButtons = ("BACK", ('0xFFFFFF'), pygame.Rect(350, 800, 300, 75))
    
    # buttons used in skin selection
    skinsBannerText = "SKIN SELECTION"
    
    skinsButtons = [
        ("RED", ('0xFF0000'), pygame.Rect(100, 225, 200, 75)),
        ("GREEN", ('0x00FF00'), pygame.Rect(400, 225, 200, 75)),
        ("BLUE", ('0x0000FF'), pygame.Rect(600, 225, 200, 75))
    ]
    
    # game variable
    playerSurface = pygame.image.load(os.path.join(scriptDir,"Sprites","sprite.png")).convert_alpha()
    playerRect = playerSurface.get_rect(midbottom=(300,800))

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    gameActive = False
    menuActive = True
    creditsActive = False
    skinsActive = False

    #Background
    roadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics","road.png")).convert_alpha()
    roadSurfaceRect = roadSurface.get_rect(topleft=(0,0))
    
    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif menuActive:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for text, color, rect in buttons:
                            if rect.collidepoint(event.pos):
                                if text == "PLAY":
                                    #IF YOU CLICK PLAY BUTTON TAKE YOU TO ACTUAL GAME
                                    #play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                    skins(screen, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                    menuActive = False
                                    creditsActive = False
                                    gameActive = False
                                elif text == "CREDITS":
                                    #IF YOU CLICK CREDITS BUTTON TAKES YOU TO CREDITS SCREEN
                                    credits(screen, menuFont, white, black, creditsActive, creditsButtons)
                                elif text == "QUIT":
                                    #IF YOU CLICK QUIT BUTTON CLOSES WINDOW
                                    pygame.quit()
                                    sys.exit()

        #if the game is not active and the menu is active take to menu and add title
        if not gameActive and menuActive:
            print("menuActive")
            menu(screen, menuFont, buttons, menuActive)
            title(screen, titleFont, titleText, white)

        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)

    # quit
    pygame.quit()

if __name__ == "__main__":
    main()
