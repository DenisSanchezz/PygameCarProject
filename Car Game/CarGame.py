import pygame
import sys
import os.path
scriptDir = os.path.dirname(os.path.abspath(__file__))

def menu(screen, menuFont, menuText, buttons):
    #bg
    screen.fill('0x737373')

    #mainMenuBannerText = menuFont.render(menuText, True, ('0x000000'))
    #screen.blit(mainMenuBannerText, (150, 60))

    for text, color, rect in buttons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, ('0x000000'))
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
def title(screen, TitleFont, TitleText, white):
    MainText = TitleFont.render(TitleText, True, white)
    screen.blit(MainText, (250, 100))

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

    titleFont = pygame.font.SysFont("Consolas", 40)
    titleText = "The Swift and the Sulky"

    # list to store all the buttons text, color, and position
    buttons = [
        ("PLAY", ('0x00FF00'), pygame.Rect(350, 225, 300, 75)),
        ("CREDITS", ('0xFFFF00'), pygame.Rect(350, 325, 300, 75)),
        ("QUIT", ('0xFF0000'), pygame.Rect(350, 425, 300, 75))
    ]

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    gameActive = False
    menuActive = True

    #Background
    RoadSurface = pygame.image.load(os.path.join(scriptDir,"Sprites/Background","Menu.png")).convert_alpha()
    screen.blit(RoadSurface, (0, 0))

    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for text, color, rect in buttons:
                        if rect.collidepoint(event.pos):
                            if text == "PLAY":
                                print("PLAY")
                            elif text == "CREDITS":
                                print("CREDITS")
                            elif text == "QUIT":
                                print("QUIT")
                                pygame.quit()
                                sys.exit()

        if not gameActive and menuActive:
            menu(screen, menuFont, menuText, buttons)
            title(screen, titleFont, titleText, white)

        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)

    # quit
    pygame.quit()

if __name__ == "__main__":
    main()
