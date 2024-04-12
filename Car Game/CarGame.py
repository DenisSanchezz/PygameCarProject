import pygame

def menu(screen, menuFont, menuText, textColor):
    #bg
    screen.fill('0x737373')
    #rectangles to overlay menu text on
    pygame.draw.rect(screen, "0x000000", [75, 30, 350, 130], 100)
    pygame.draw.rect(screen, "0xFFFFFF", [75, 30, 350, 130], 10)
    
    #render the text
    mainMenuBannerText = menuFont.render(menuText, True, textColor)
    screen.blit(mainMenuBannerText, (150, 60))
    
    

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
    textColor = ('0xFFFFFF')
    menuText = "Main Menu"

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    game_active = False

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
