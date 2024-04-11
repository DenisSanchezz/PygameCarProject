import pygame

def main():
    # setup
    pygame.init()
    
    screenWidth = 750
    screenHeight = 900
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("The Swift and the Sulky")
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color 
        screen.fill("black")

        # update()
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
