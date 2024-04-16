# Example file showing a basic pygame "game loop"
import pygame
import os.path
scriptDir = os.path.dirname(os.path.abspath(__file__))
# pygame setup




def menu(screen, menuFont, menuText, textColor):
    mainMenuBannerText = menuFont.render(menuText, True, textColor)
    screen.blit(mainMenuBannerText, (400, 300))

def Title(screen, TitleFont, TitleText, textColor):
    MainText = TitleFont.render(TitleText, True, textColor)
    screen.blit(MainText, (250, 100))

def main():
    # init()
    pygame.init()

    # setup the screen
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('The Swift and the Sulky')
    #GameName
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error


    # setup the menu variables
    menuFont = pygame.font.SysFont("Consolas", 40)
    textColor = (255, 255, 255)
    menuText = "Main Menu"
    # render text
    TitleFont = pygame.font.SysFont("Consolas", 40)
    TitleText = "The Swift and the Sulky"
    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    game_active = False
    #Background
    RoadSurface = pygame.image.load(os.path.join(scriptDir,"Sprites/Background","Menu.png")).convert_alpha()
    screen.blit(RoadSurface, (0, 0))
    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_active:
            menu(screen, menuFont, menuText, textColor)
            Title(screen, TitleFont, TitleText, textColor)
        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)

    # quit
    pygame.quit()

if __name__ == "__main__":
    main()
