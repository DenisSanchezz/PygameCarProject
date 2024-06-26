import pygame
import sys
import os.path
import random
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

def instructions(screen, menuFont, white, black, instructionsActive, instructionsButtons):
    screen.fill(black)
    
    backButton = pygame.draw.rect(screen, instructionsButtons[1], instructionsButtons[2], 0)
    backButtonText = menuFont.render(instructionsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)

    #   PUT INSTRUCTIONS HERE
    instructionsText1 = menuFont.render("INSTRUCTIONS",                                  
                                    True, white)
    
    instructionsText2 = menuFont.render("Use WASD to move around",                                  
                                    True, white)
    
    instructionsText3 = menuFont.render("Avoid obstacles such as cones",                                  
                                    True, white)
    instructionsText4 = menuFont.render("Watch out for incoming enemy cars",                                  
                                    True, white)
    instructionsText5 = menuFont.render("Last as long as you can!",                                  
                                    True, white)
    
    screen.blit(instructionsText1, (350, 60))
    screen.blit(instructionsText2, (220, 140))
    screen.blit(instructionsText3, (180, 220))
    screen.blit(instructionsText4, (115, 280))
    screen.blit(instructionsText5, (220, 340))
    screen.blit(backButtonText, backButtonTextRect)

    instructionsActive = True
    pygame.display.update()
    
    while instructionsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.collidepoint(event.pos):
                        instructionsActive = False

def credits(screen, menuFont, white, black, creditsActive, creditsButtons):
    screen.fill(black)
    
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)

    #   PUT CREDITS HERE
    creditsText1 = menuFont.render("| THE FLYING BEARS |",                                  
                                    True, white)
    
    creditsText2 = menuFont.render("DEVELOPER TEAM",                                  
                                    True, white)
    
    creditsText3 = menuFont.render("Braeden Boyce",                                  
                                    True, white)
    creditsText4 = menuFont.render("Charles Pope",                                  
                                    True, white)
    creditsText5 = menuFont.render("Denis Sanchez",                                  
                                    True, white)
    
    screen.blit(creditsText1, (275, 60))
    screen.blit(creditsText2, (350, 140))
    screen.blit(creditsText3, (350, 220))
    screen.blit(creditsText4, (350, 280))
    screen.blit(creditsText5, (350, 340))
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
        #print("Credits is actives")

def levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive):
    screen.fill('0x737373')
    
    levelSelectActive = True
    
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)
    
    levelSelectBanner = menuFont.render(levelSelectText, True, white)
    
    screen.blit(backButtonText, backButtonTextRect)
    screen.blit(levelSelectBanner, (365, 100))
    
    LittleRoadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleRoad.png")).convert_alpha()
    screen.blit(LittleRoadSurface,(-280,-400))
    
    LittleBeachSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleBeachRoad.png")).convert_alpha()
    screen.blit(LittleBeachSurface,(30,-200))
    
    LittleCitySurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleCityRoad.png")).convert_alpha()
    screen.blit(LittleCitySurface,(320,-390))
    
    for text, color, rect in levelSelectButtons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, white)
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
    pygame.display.update()
    while levelSelectActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for text, color, rect in levelSelectButtons:
                        if rect.collidepoint(event.pos):
                            if text == "Level 1":
                                roadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","road.png")).convert_alpha()
                                roadSurfaceRect = roadSurface.get_rect(topleft=(0,0))
                                
                                skins(screen, playerX, playerY, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, levelSelectActive, levelSelectButtons, levelSelectText, menuActive)
                                
                                levelSelectActive = False
                            elif text == "Level 2":
                                roadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","BeachRoad.png")).convert_alpha()
                                roadSurfaceRect = roadSurface.get_rect(topleft=(0,0))
                                
                                skins(screen, playerX, playerY, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, levelSelectActive, levelSelectButtons, levelSelectText, menuActive)
                                
                                levelSelectActive = False
                            elif text == "Level 3":
                                roadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","CityRoad.png")).convert_alpha()
                                roadSurfaceRect = roadSurface.get_rect(topleft=(0,0))
                                
                                skins(screen, playerX, playerY, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, levelSelectActive, levelSelectButtons, levelSelectText, menuActive)
                                
                                levelSelectActive = False
                    if backButton.collidepoint(event.pos):
                        #change so it goes to the level screen 
                        main()
                        menuActive = True
                        levelSelectActive = False

def skins(screen, playerX, playerY, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, levelSelectActive, levelSelectButtons, levelSelectText, menuActive):
    screen.fill('0x737373')
    
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)
    
    skinsBanner = menuFont.render(skinsBannerText, True, white)
    
    screen.blit(backButtonText, backButtonTextRect)
    screen.blit(skinsBanner, (330, 100))
    
    for text, color, rect in skinsButtons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, black)
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
                    for text, color, rect in skinsButtons:
                        if rect.collidepoint(event.pos):
                            if text == "Red":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","RedCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                skinsActive = False
                            elif text == "Black":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","BlackCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                skinsActive = False
                            elif text == "Blue":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","BlueCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                skinsActive = False
                            elif text == "White":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","WhiteCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                skinsActive = False
                            elif text == "Yellow":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","YellowCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                skinsActive = False
                    if backButton.collidepoint(event.pos):
                        #change so it goes to the level screen 
                        levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive)
                        levelSelectActive = True
                        skinsActive = False
        #print("Skins is active")

def play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect):
    
    #fill screen to remove the menu stuff
    screen.fill(black)

    #ai cars stuff
    npcX = 0
    npcY = -200  #the starting position offscreen

    npcSurface = pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites","NPCRedCar.png")).convert_alpha()
    npcRect = npcSurface.get_rect(midbottom=(npcX, npcY))

    #list for car sprites
    npcCarSprites = [
        #paths
        "YellowCar.png",
        "WhiteCar.png",
        "BlueCar.png",
        "BlackCar.png",
        "NPCRedCar.png"
    ]
    
    npcSpawnRate = 0.01
    npcSpeed = 0.6 #adjust to whatever speed the ai car should go
    
    #list to hold cars
    npcCars = []

    #list to hold surfaces for the npcs
    npcSurfaces = []
    
    for spritePath in npcCarSprites:
        npcSurfaces.append(pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites", spritePath)).convert_alpha())
    
    #obstacles
    #575
    barrierX = 725
    barrierY = 600
    
    barrierObstacle = pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites","ObstacleOne.png")).convert_alpha()
    barrierObstacleRect = barrierObstacle.get_rect(midbottom=(barrierX, barrierY))
    
    barrierSpawnRate = 0.005 #0.005
    barrierSpeed = 1
    
    barriers = []
    
    #player speed adjust to whatever
    playerSpeed = 1

    #boolean to check if keys are being held down
    moveRight = False
    moveLeft = False
    
    gameActive = True
    pygame.display.update()

    while gameActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moveRight = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moveLeft = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moveRight = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moveLeft = False

        #player movement
        if moveRight:
            playerX += playerSpeed
        if moveLeft:
            playerX -= playerSpeed

        #spawning cars 
        if random.random() < npcSpawnRate:

            #randomNPCCar = random.choice(npcCarSprites)
            #npcSurface = npcSurfaces[npcCarSprites.index(randomNPCCar)]

            #checks if there's enough space for a new car so they do not overlap
            spawnNewCar = True
            for npcRect in npcCars:
                if abs(npcRect.x - npcX) < npcRect.width * 2:
                    #if the distance between the cars is too close 
                    spawnNewCar = False
                    break
            
            #if there is enough space for a new car
            if spawnNewCar:
                leftLane = random.randint(1, 2)  #randomly select a lane on the left
                npcX = 275 if leftLane == 1 else 425
                npcY = -200  #off screen coordinate
                npcRect = npcSurface.get_rect(midbottom=(npcX, npcY))
                npcCars.append(npcRect)

        #ai car movement and if the player hits one
        for npcRect in npcCars[:]:
            npcRect.y += npcSpeed  #update car position
            if npcRect.y > 1000:  #if the car goes off screen remove it
                npcCars.remove(npcRect)  
            if playerRect.colliderect(npcRect):
                #put logic for when the player hits another car here
                #
                print("you hit a car")
        
        if random.random() < barrierSpawnRate:
            spawnNewBarrier = True
            for barrierObstacleRect in barriers:
                if abs(barrierObstacleRect.x - barrierX) < barrierObstacleRect.width * 2:
                    spawnNewBarrier = False
                    break
            
            if spawnNewBarrier:
                rightLane = random.randint(1, 2)
                barrierX = 575 if rightLane == 1 else 725
                barrierY = -100
                barrierObstacleRect = barrierObstacle.get_rect(midbottom=(barrierX, barrierY))
                barriers.append(barrierObstacleRect)
        
        for barrierObstacleRect in barriers[:]:
            barrierObstacleRect.y += barrierSpeed #figure out how to make this lower than 1
            if barrierObstacleRect.y > 1000:
                barriers.remove(barrierObstacleRect)
            if playerRect.colliderect(barrierObstacleRect):
                print("you hit the barrier")

        print(barrierObstacleRect.y)
        #road boundaries
        playerX = max(170, min(775, playerX))

        #updates the players position
        playerRect.x = playerX
        
        #redraws the screen
        screen.fill(black)
        screen.blit(roadSurface, roadSurfaceRect)
        screen.blit(playerSurface, playerRect)
        screen.blit(npcSurface, npcRect)
        screen.blit(barrierObstacle, barrierObstacleRect)
        
        
        #update display
        pygame.display.update()

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

    # main menu buttons
    buttons = [
        ("PLAY", ('0x00FF00'), pygame.Rect(350, 225, 300, 75)),
        ("INSTRUCTIONS", ('0x0000FF'), pygame.Rect(350, 325, 300, 75)),
        ("CREDITS", ('0xFFFF00'), pygame.Rect(350, 425, 300, 75)),
        ("QUIT", ('0xFF0000'), pygame.Rect(350, 525, 300, 75))
    ]

    # credits screen variables
    instructionsButtons = ("BACK", ('0xFFFFFF'), pygame.Rect(350, 800, 300, 75))

    creditsButtons = ("BACK", ('0xFFFFFF'), pygame.Rect(350, 800, 300, 75))
    
    # skin select variables
    skinsBannerText = "SKIN SELECTION"
    skinsButtons = [
        ("Red", ('0xFF0000'), pygame.Rect(100, 225, 200, 75)),
        ("Black", ('0x4d4d4d'), pygame.Rect(400, 225, 200, 75)),
        ("Blue", ('0x0000FF'), pygame.Rect(700, 225, 200, 75)),
        ("White", ('0xFFFFFF'), pygame.Rect(100, 425, 200, 75)),
        ("Yellow", ('0xFFFF00'), pygame.Rect(400, 425, 200, 75))
    ]
    
    # level select variables
    levelSelectButtons = [
        ("Level 1", ('0x000000'), pygame.Rect(100, 225, 200, 75)),
        ("Level 2", ('0x000000'), pygame.Rect(400, 225, 200, 75)),
        ("Level 3", ('0x000000'), pygame.Rect(700, 225, 200, 75))
    ]
    levelSelectText = "Select Level"
    
    # player variable
    playerX = 545
    playerY = 800
    
    #playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","sprite.png")).convert_alpha()
    #playerRect = playerSurface.get_rect(midbottom=(300,800))

    # loop variables
    fps = 60
    clock = pygame.time.Clock()
    running = True
    gameActive = False
    menuActive = True
    instructionsActive=False
    creditsActive = False
    skinsActive = False
    levelSelectActive = False
    
    # Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if menuActive:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for text, color, rect in buttons:
                            if rect.collidepoint(event.pos):
                                if text == "PLAY":
                                    #IF YOU CLICK PLAY BUTTON TAKE YOU TO ACTUAL GAME
                                    #play(screen, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                    levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive)
                                    #skins(screen, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect)
                                    menuActive = False
                                    instructionsActive=False
                                    creditsActive = False
                                    gameActive = False
                                elif text == "CREDITS":
                                    #IF YOU CLICK CREDITS BUTTON TAKES YOU TO CREDITS SCREEN
                                    credits(screen, menuFont, white, black, creditsActive, creditsButtons)
                                elif text == "INSTRUCTIONS":
                                    instructions(screen, menuFont, white, black, creditsActive, instructionsButtons)
                                elif text == "QUIT":
                                    #IF YOU CLICK QUIT BUTTON CLOSES WINDOW
                                    pygame.quit()
                                    sys.exit()

        #if the game is not active and the menu is active take to menu and add title
        if not gameActive and menuActive:
            #print("menuActive")
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
