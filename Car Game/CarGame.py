import pygame

def menu(screen, menuFont, menuText, playText, creditsText, quitText, whiteTextColor, blackTextColor):
    #bg
    screen.fill('0x737373')
    
    #gets mouse position to check if mouse is on a rect (play, exit, etc)
    mouseX, mouseY = pygame.mouse.get_pos()
    
    #rectangles to overlay menu text on
    pygame.draw.rect(screen, "0x000000", [75, 30, 350, 130], 100)
    pygame.draw.rect(screen, "0xFFFFFF", [75, 30, 350, 130], 10)
    
    #create menu buttons
    pygame.draw.rect(screen, "0xFFFFFF", [100, 225, 300, 75], 100)
    pygame.draw.rect(screen, "0x00FF00", [100, 225, 300, 75], 10)
    
    pygame.draw.rect(screen, "0xFFFFFF", [100, 325, 300, 75], 100)
    pygame.draw.rect(screen, "0xFFFF00", [100, 325, 300, 75], 10)
    
    pygame.draw.rect(screen, "0xFFFFFF", [100, 425, 300, 75], 100)
    pygame.draw.rect(screen, "0xFF0000", [100, 425, 300, 75], 10)
    
    #render the text
    mainMenuBannerText = menuFont.render(menuText, True, whiteTextColor)
    playButtonText = menuFont.render(playText, True, blackTextColor)
    creditsButtonText = menuFont.render(creditsText, True, blackTextColor)
    quitButtonText = menuFont.render(quitText, True, blackTextColor)
    
    screen.blit(mainMenuBannerText, (150, 60))
    screen.blit(playButtonText, (200, 240))
    screen.blit(creditsButtonText, (165, 340))
    screen.blit(quitButtonText, (200, 440))

def main():
    # init()
    pygame.init()

    # setup the screen
    screen_width = 500
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('The Swift and the Sulky')

    # setup the menu variables
    menuFont = pygame.font.SysFont("Consolas", 40, bold=True)
    whiteTextColor = ('0xFFFFFF')
    blackTextColor = ('0x000000')
    
    menuText = "Main Menu"
    playText = "PLAY"
    creditsText = "CREDITS"
    quitText = "QUIT"

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    gameActive = False
    menuActive = True

    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not gameActive and menuActive:
            menu(screen, menuFont, menuText, playText, creditsText, quitText, whiteTextColor, blackTextColor)

        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)

    # quit
    pygame.quit()

if __name__ == "__main__":
    main()
