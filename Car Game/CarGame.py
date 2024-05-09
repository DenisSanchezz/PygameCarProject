import pygame
import sys
import os.path
import random

# os file path
scriptDir = os.path.dirname(os.path.abspath(__file__))

def menu(screen, menuFont, buttons):
    # Variables for the background of the main menu
    startscreen = pygame.image.load(os.path.join(scriptDir,"Graphics/","titlescreen.png")).convert_alpha()
    screen.blit(startscreen,(0,0))

    # For every text, color, and rect in the menu buttons list
    # draw them onto the screen using the color and rect
    # render the text from the text
    # get text rect
    # blit the text to the screen
    for text, color, rect in buttons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, ('0x000000'))
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
def title(screen, TitleFont, TitleText, white):
    # Variables for the title
    mainText = TitleFont.render(TitleText, True, white)
    screen.blit(mainText, (127, 100))

def instructions(screen, menuFont, white, black, instructionsActive, instructionsButtons):
    # Clears the screen and sets the background to black
    screen.fill(black)
    
    # Variables for back button
    backButton = pygame.draw.rect(screen, instructionsButtons[1], instructionsButtons[2], 0)
    backButtonText = menuFont.render(instructionsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)

    # Renders text that details how to play the game
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
    
    # Blits the text
    screen.blit(instructionsText1, (350, 60))
    screen.blit(instructionsText2, (220, 140))
    screen.blit(instructionsText3, (180, 220))
    screen.blit(instructionsText4, (115, 280))
    screen.blit(instructionsText5, (220, 340))
    screen.blit(backButtonText, backButtonTextRect)

    # Boolean set to true to indicate that the loop is active
    instructionsActive = True
    # Update
    pygame.display.update()
    
    while instructionsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.collidepoint(event.pos):
                        #If the left mouse button clicks back button takes out of this loop
                        instructionsActive = False

def credits(screen, smallCreditsFont, creditsFont, menuFont, white, black, creditsActive, creditsButtons):
    # Clears the screen adn sets background color to black
    screen.fill(black)
    
    # Variables for back button to the menu
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)

    # Renders text for the credits of the developer team
    creditsText1 = creditsFont.render("| THE FLYING BEARS |",                                  
                                    True, white)
    
    creditsText2 = creditsFont.render("DEVELOPER TEAM",                                  
                                    True, white)
    
    creditsText3 = creditsFont.render("Braeden Boyce",                                  
                                    True, white)
    creditsText4 = creditsFont.render("Charles Pope",                                  
                                    True, white)
    creditsText5 = creditsFont.render("Denis Sanchez",                                  
                                    True, white)
    creditsText6 = smallCreditsFont.render("Main Menu Background - https://www.wallpaperflare.com/need-for-speed-need-for-speed-heat-wallpaper-giisx/download", True, white)
    creditsText7 = smallCreditsFont.render("Car Sprites - https://tokka.itch.io/top-down-car", True, white)
    creditsText8 = smallCreditsFont.render("Road - https://opengameart.org/content/2d-top-down-highway-background", True, white)
    
    # Blits the text
    screen.blit(creditsText1, (0, 30))
    screen.blit(creditsText2, (50, 110))
    screen.blit(creditsText3, (50, 190))
    screen.blit(creditsText4, (50, 250))
    screen.blit(creditsText5, (50, 310))
    screen.blit(creditsText6, (50, 370))
    screen.blit(creditsText7, (50, 390))
    screen.blit(creditsText8, (50, 410))
    screen.blit(backButtonText, backButtonTextRect)

    # Sets boolean to true to indicate that this loop is active
    creditsActive = True
    #Update
    pygame.display.update()

    while creditsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.collidepoint(event.pos):
                        #Disables this loop if the left mouse button clicks the back button
                        creditsActive = False

def levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive):
    # Fills the screen with grey and removes previous surfaces on screen
    screen.fill('0x737373')
    
    # Sets boolean to true to indicate
    # that this menu is active
    levelSelectActive = True
    
    # Creates variables for a back button to go back to the previous menu
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)
    
    # Renders the text at the top of the screen that indicates where the user is
    levelSelectBanner = menuFont.render(levelSelectText, True, white)
    
    # Blits the back button and level selection text to the screen
    screen.blit(backButtonText, backButtonTextRect)
    screen.blit(levelSelectBanner, (365, 100))
    
    # A small version of the map to show what the map looks like that you are selecting
    LittleRoadSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleRoad.png")).convert_alpha()
    screen.blit(LittleRoadSurface,(-280,-400))
    
    LittleBeachSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleBeachRoad.png")).convert_alpha()
    screen.blit(LittleBeachSurface,(30,-200))
    
    LittleCitySurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Maps","LittleCityRoad.png")).convert_alpha()
    screen.blit(LittleCitySurface,(320,-390))
    
    # For every text, color, and rect in the level select buttons list
    # Draw the buttons on the screen at the rects position
    # create a text variable using the text from the list
    # get the rect from the text
    # blit the texts
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
            # checks if the left mouse button is clicked
            # while collided with the text for the different levels
            # if so then sets the road surface to the level selected 
            # takes to the skins menu
            # and disables this loop
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
                        #If this is clicked then takes back the the main menu screen 
                        # Disables this loop and enables the menu loop
                        main()
                        menuActive = True
                        levelSelectActive = False

def skins(screen, playerX, playerY, skinsActive, white, black, menuFont, skinsButtons, skinsBannerText, creditsButtons, gameActive, roadSurface, roadSurfaceRect, levelSelectActive, levelSelectButtons, levelSelectText, menuActive):
    # Clears the screen and sets it to a light grey
    screen.fill('0x737373')
    
    # Variables for a back button
    backButton = pygame.draw.rect(screen, creditsButtons[1], creditsButtons[2], 0)
    backButtonText = menuFont.render(creditsButtons[0], True, black)
    backButtonTextRect = backButtonText.get_rect(center=backButton.center)
    
    # Renders the skins banner text to the top of the screen to indicate where the user is
    skinsBanner = menuFont.render(skinsBannerText, True, white)
    
    # Blit the backbutton and skin text
    screen.blit(backButtonText, backButtonTextRect)
    screen.blit(skinsBanner, (330, 100))
    
    # For every text, color, and rect in the skins buttons list 
    # it draws the button, creates the text, gets the rect of the text, and blits
    for text, color, rect in skinsButtons:
        pygame.draw.rect(screen, color, rect, 0)
        buttonText = menuFont.render(text, True, black)
        textRect = buttonText.get_rect(center=rect.center)
        screen.blit(buttonText, textRect)
    
    # Boolean to indicate that this screen and loop is active
    skinsActive = True
    
    pygame.display.update()
    while skinsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Checks if the left mouse button is clicked
            # on one of the skins rects
            # If the mouse is clicked on one of the skins rects 
            # it sets the player to that skin, starts the game, and disables this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for text, color, rect in skinsButtons:
                        if rect.collidepoint(event.pos):
                            if text == "Red":
                                playerSurface = pygame.image.load(os.path.join(scriptDir,"Graphics/Sprites","RedCar.png")).convert_alpha()
                                playerRect = playerSurface.get_rect(midbottom=(playerX,playerY))
                                #play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
                                countdown(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect)
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
                    # Checks if the left mouse button is clicked 
                    # while collided with the back button
                    # if so then take back to the previous menu (level selection)
                    if backButton.collidepoint(event.pos): 
                        levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive)
                        levelSelectActive = True
                        skinsActive = False

def countdown(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect):
    screen.fill(black)
    
    countdownActive = True
    pygame.display.update
    
    while countdownActive:
        pass

def play(screen, playerX, playerY, gameActive, black, roadSurface, roadSurfaceRect, playerSurface, playerRect):
    
    # Fill the screen to remove what was on it previously
    screen.fill(black)

    # Starting coordinates for the AI cars that spawn and go down the screen
    npcX = 0
    npcY = -200  # The starting position off the screen

    # Loads the inverted player car for the NPC cars
    npcSurface = pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites","NPCRedCar.png")).convert_alpha()
    # Rect for the npc surface using the coordinates
    npcRect = npcSurface.get_rect(midbottom=(npcX, npcY))

    # List of sprites for the npc cars
    npcCarSprites = [
        "YellowCar.png",
        "WhiteCar.png",
        "BlueCar.png",
        "BlackCar.png",
        "NPCRedCar.png"
    ]
    
    # Spawnrate of the npcs
    npcSpawnRate = 0.01
    npcSpeed = 0.6 # need to figure out how to make this lower
    
    # List for the cars 
    npcCars = []

    # List to hold surfaces (doesnt work yet)
    npcSurfaces = []
    
    # for every sprite path in the list of paths
    for spritePath in npcCarSprites:
        # append it to the list of surfaces
        npcSurfaces.append(pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites", spritePath)).convert_alpha())
    
    # The barrier obstacles corridinates
    barrierX = 725
    barrierY = 600
    
    # makes surface and rect for barrier
    barrierObstacle = pygame.image.load(os.path.join(scriptDir, "Graphics/Sprites","ObstacleOne.png")).convert_alpha()
    barrierObstacleRect = barrierObstacle.get_rect(midbottom=(barrierX, barrierY))
    
    # spawnrate of barriers
    barrierSpawnRate = 0.005 #0.005
    # speed of barriers
    barrierSpeed = 1
    
    # list to hold barriers
    barriers = []
    
    # The speed of the player
    playerSpeed = 1

    # Booleans for the movement of the player
    moveRight = False
    moveLeft = False

    gameActive = True
    pygame.display.update()

    while gameActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # If the key is being held down
            # check what key it is and if its D or Right then movement is true
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moveRight = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moveLeft = True
            # If the key not being held down anymore
            # check what key if its D or Right and make movement false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moveRight = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moveLeft = False

        # If either move boolean is true add the respective amount of speed to the X
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
                print("you hit a barrier")
                pass

        print(barrierObstacleRect.y)
        
        # The boundaries of the road (sets boundaries so player cannot move off the road and screen)
        playerX = max(170, min(775, playerX))

        # Update the player position
        playerRect.x = playerX
        
        # Redraw the screen
        screen.fill(black)
        screen.blit(roadSurface, roadSurfaceRect)
        screen.blit(playerSurface, playerRect)
        screen.blit(npcSurface, npcRect)
        screen.blit(barrierObstacle, barrierObstacleRect)
        
        
        # Update the display
        pygame.display.update()

def main():
    # Setup
    pygame.init()

    # Setup for the screen and window
    screenWidth = 1000
    screenHeight = 1000
    
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('The Swift and the Sulky')

    # Setup the variables used in the Main Menu
    menuFont = pygame.font.SysFont("Consolas", 40, bold=True)
    menuText = "Main Menu"
    
    white = '0xFFFFFF'
    black = '0x000000'

    titleFont = pygame.font.SysFont("Consolas", 60, bold=True)
    titleText = "The Swift and the Sulky"

    # A list to contain the data for the buttons used in the Main Menu
    buttons = [
        ("PLAY", ('0x00FF00'), pygame.Rect(350, 225, 300, 75)),
        ("INSTRUCTIONS", ('0x0000FF'), pygame.Rect(350, 325, 300, 75)),
        ("CREDITS", ('0xFFFF00'), pygame.Rect(350, 425, 300, 75)),
        ("QUIT", ('0xFF0000'), pygame.Rect(350, 525, 300, 75))
    ]

    # Setup variables used in the Credits and Instructions Screen
    instructionsButtons = ("BACK", ('0xFFFFFF'), pygame.Rect(350, 800, 300, 75))
    
    creditsButtons = ("BACK", ('0xFFFFFF'), pygame.Rect(350, 800, 300, 75))
    
    creditsFont = pygame.font.SysFont("Consolas", 30, bold=True)
    smallCreditsFont = pygame.font.SysFont("Consolas", 15)
    
    # Setup Variables for the Skin Selection screens
    skinsBannerText = "SKIN SELECTION" # text on the top of the screen to label where you are 
    
    # A list to contain the data for the buttons used in Skin Selection
    skinsButtons = [
        ("Red", ('0xFF0000'), pygame.Rect(100, 225, 200, 75)),
        ("Black", ('0x4d4d4d'), pygame.Rect(400, 225, 200, 75)),
        ("Blue", ('0x0000FF'), pygame.Rect(700, 225, 200, 75)),
        ("White", ('0xFFFFFF'), pygame.Rect(100, 425, 200, 75)),
        ("Yellow", ('0xFFFF00'), pygame.Rect(400, 425, 200, 75))
    ]
    
    # Setup Variables for Level Selection
    
    # A list to contain the data for the buttons used in Level Selection
    levelSelectButtons = [
        ("Level 1", ('0x000000'), pygame.Rect(100, 225, 200, 75)),
        ("Level 2", ('0x000000'), pygame.Rect(400, 225, 200, 75)),
        ("Level 3", ('0x000000'), pygame.Rect(700, 225, 200, 75))
    ]
    
    # Text at the top of the screen to indicate where you are
    levelSelectText = "Select Level"
    
    # Variables for the players position
    playerX = 545
    playerY = 800

    # Variables used in the loop of the game
    fps = 60
    clock = pygame.time.Clock()
    
    # Booleans to indicate what screens should be active
    running = True
    gameActive = False
    menuActive = True
    instructionsActive= False
    creditsActive = False
    skinsActive = False
    levelSelectActive = False
    
    # While loop for that takes to main menu
    while running:
        for event in pygame.event.get():
            # Exits out of the window if the user clicks the exit button
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            """
            If the menuActive variable is true
            Checks for left mouse clicks
            Gets the text, color, and rect position for each button
            If the mouse collides with the rect and the left mouse button is clicked then takes you to the menu that you clicked on
            """
            if menuActive:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for text, color, rect in buttons:
                            if rect.collidepoint(event.pos):
                                if text == "PLAY":
                                    # If you click the play button takes you into the process of starting the game
                                    
                                    # First takes the user to what level they want to play
                                    levelSelect(screen, playerX, playerY, levelSelectActive, white, black, menuFont, levelSelectButtons, levelSelectText, creditsButtons, menuActive, gameActive, skinsButtons, skinsBannerText, skinsActive)
                                    
                                    # Makes sure booleans are false
                                    instructionsActive=False
                                    creditsActive = False
                                    gameActive = False
                                    
                                    # Takes the user out of this if statement
                                    menuActive = False
                                    
                                elif text == "CREDITS":
                                    # If you click the credits button then it takes you to the credits screen
                                    credits(screen, smallCreditsFont, creditsFont, menuFont, white, black, creditsActive, creditsButtons)
                                    
                                elif text == "INSTRUCTIONS":
                                    # If the mouse clicks the rect with "INSTRUCTIONS" then takes you to the instructions screen
                                    instructions(screen, menuFont, white, black, creditsActive, instructionsButtons)
                                    
                                elif text == "QUIT":
                                    # If the mouse clicks the rect with "QUIT" on it then quits and exits the game
                                    pygame.quit()
                                    sys.exit()

        # If the game is not active and the menu IS active
        # takes you to menu screen
        if not gameActive and menuActive:
            menu(screen, menuFont, buttons)
            title(screen, titleFont, titleText, white)

        # Update display
        pygame.display.update()
        
        # FPS
        clock.tick(fps)
    
    pygame.quit()

# Takes to main method when code is run
if __name__ == "__main__":
    main()
