# code for developing car racing game in python
import pygame
import time
import random
import math

# initialize pygame and set the colors
pygame.init()

WIDTH, HEIGHT = 800, 800

gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

gamedisplays = pygame.display.set_mode(
    (WIDTH, HEIGHT))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()
carimg = pygame.image.load('car1.jpg')
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")
car_width = 56
pause = False

# Intro screen
def intro_loop():
    intro = True
    while intro:

        # Quit Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        
        # Background
        gamedisplays.blit(intro_background, (0, 0))
        
        # Title Text
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (WIDTH // 2, HEIGHT // 2 - 100)
        gamedisplays.blit(TextSurf, TextRect)

        # Buttons
        button("START", WIDTH // 2 - 300, HEIGHT // 2, 
               200, 50, green, bright_green, "play")
        button("INSTRUCTION", WIDTH // 2, HEIGHT // 2, 
               200, 50, blue, bright_blue, "intro")
        button("QUIT", WIDTH // 2 + 300, HEIGHT // 2, 
               200, 50, red, bright_red, "quit")
        pygame.display.update()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays,
                         ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()

    else:
        pygame.draw.rect(gamedisplays,
                         ic,
                         (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplays.blit(textsurf, textrect)

def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_objects(
            "This is an car game in which you" +
            "need dodge the coming cars", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        gamedisplays.blit(TextSurf, TextRect)
        gamedisplays.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects(
            "ARROW LEFT : LEFT TURN", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_objects(
            "ARROW RIGHT : RIGHT TURN", smalltext)
        hTextRect.center = ((150), (450))
        atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext)
        atextRect.center = ((150), (500))
        rtextSurf, rtextRect = text_objects("B : BRAKE ", smalltext)
        rtextRect.center = ((150), (550))
        ptextSurf, ptextRect = text_objects("P : PAUSE  ", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        gamedisplays.blit(sTextSurf, sTextRect)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(hTextSurf, hTextRect)
        gamedisplays.blit(atextSurf, atextRect)
        gamedisplays.blit(rtextSurf, rtextRect)
        gamedisplays.blit(ptextSurf, ptextRect)
        button("BACK", 600, 450, 100, 50, blue,
               bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("PAUSED", largetext)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        gamedisplays.blit(TextSurf, TextRect)
        button("CONTINUE", 150, 450,
               150, 50, green,
               bright_green, "unpause")
        button("RESTART", 350, 450, 150,
               50, blue, bright_blue,
               "play")
        button("MAIN MENU", 550, 450,
               200, 50, red, bright_red,
               "menu")
        pygame.display.update()
        clock.tick(30)

def unpaused():
    global pause
    pause = False

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def crash():
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects("YOU CRASHED", largetext)
    textrect.center = (
        (WIDTH/2),
        (HEIGHT/2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def win():
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects("YOU WIN", largetext)
    textrect.center = (
        (WIDTH/2),
        (HEIGHT/2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def car(x, y):
    gamedisplays.blit(carimg, (x, y))

def game_loop():
    global pause

    # ---------------------------------------
    # Initialize
    # ---------------------------------------
    
    # 0. Overhead Setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # 1. World Setup
    TRACK_LENGTH = 5000         # 5000 pixels = 312.5 meters
    FINISH_LINE_Y = 0.0         # Finish line near the top of the world

    # 2. Camera Settings
    CAR_SCREEN_Y = HEIGHT - 150 # Car is drawn 150 pixels from the bottom of the screen

    # 3. Car Surface (for drawing)
    car_surf = pygame.Surface((36, 72), pygame.SRCALPHA)
    pygame.draw.rect(car_surf, (220, 40, 40), (0, 0, 36, 72), border_radius=6)
    pygame.draw.rect(
        car_surf, (40, 40, 50), (4, 14, 28, 16)
    )  # Windshield (shows front)

    # 4. Car State Variables
    car_y = TRACK_LENGTH        # In pixels, start at the bottom of the track
    car_x = WIDTH // 2 - 20     # In pixels, center the car horizontally on the track

    car_y_m = car_y / 16.0  # In meters. Initialised local variable to avoid UnboundLocalError
    car_x_m = car_x / 16.0 
    speed = 0.0      # In meters per second
    car_angle = 0.0  # In degrees, 0 is straight up the track.

    # 4. Car Physics Settings
    PIXELS_PER_METER = 16.0 # Scaling Constant: 16 pixels = 1 meter

    MAX_SPEED = 55.0
    ACCELERATION = 6.5
    BRAKE_FORCE = 10.0
    FRICTION = 1.5
    TURN_SPEED = 90.0 # Degrees per second
    
    # ---------------------------------------
    # Game Loop
    # ---------------------------------------
    running = True
    while running:

        # 0. Delta Time Calculation
        dt = clock.tick(60) / 1000 #Caps to 60 ticks per second
        dt = max(0.001, min(0.1, dt)) #Caps delta time to milliseconds intervals.

        pause = True
        
        # 1. Input Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 1.1 Forward Acceleration and Braking
        # True meat of the game loop. This is where we update the speed based on user input.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:           #Accelerate
            speed += ACCELERATION * dt
        elif keys[pygame.K_DOWN]:       #Brake
            speed = max(0.0, speed - BRAKE_FORCE * dt)
        else:                           #Apply friction when no input is given
            speed = max(0.0, speed - FRICTION * dt)
        speed = min(speed, MAX_SPEED) #Cap speed to max speed

        # 1.2. Steering
        turn_factor = min(1.0, speed / 8.0)  # Only turns when moving. Reaches full turn response at 8 m/s
        if keys[pygame.K_LEFT]:
            car_angle += TURN_SPEED * turn_factor * dt
        if keys[pygame.K_RIGHT]:
            car_angle -= TURN_SPEED * turn_factor * dt
        car_angle = max(-75.0, min(75.0, car_angle)) # Cap the car's angle.

        # 2. Update Car World Position
        rad = math.radians(car_angle) #Vector Normalization.   
        car_x_m -= math.sin(rad) * speed * dt
        car_y_m -= math.cos(rad) * speed * dt

        car_x = car_x_m * PIXELS_PER_METER  # Convert speed from meters to pixels and update position
        car_y = car_y_m * PIXELS_PER_METER  # Convert speed from meters to pixels and update position
        camera_y = car_y - CAR_SCREEN_Y # Update Car Screen Position

        # 3. Draw Everything (World Y -> Screen Y)
        screen.fill((40, 140, 40))  # Grass

        # Road
        pygame.draw.rect(screen, (50, 50, 50), (WIDTH // 2 - 150, 0, 300, HEIGHT))

        # Dashed center lines (drawn in world space so they scroll past!)
        for world_line_y in range(0, TRACK_LENGTH + HEIGHT, 120):
            screen_line_y = world_line_y - camera_y
            if -60 <= screen_line_y <= HEIGHT:  # Only draw if visible on screen
                pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 5, screen_line_y, 10, 60))

        # Finish Line
        finish_screen_y = FINISH_LINE_Y - camera_y
        pygame.draw.rect(screen, (255, 215, 0), (WIDTH // 2 - 150, finish_screen_y, 300, 20))

        # Player Car (always draws at CAR_SCREEN_Y)
        rotated_car = pygame.transform.rotate(car_surf, car_angle)
        car_rect = rotated_car.get_rect(center=(car_x, CAR_SCREEN_Y))
        screen.blit(rotated_car, car_rect.topleft)

        # 5. Check Conditions
        if car_y <= FINISH_LINE_Y:
            win()

        button("Pause", WIDTH - 150, 0, 150, 50, blue, bright_blue, "pause")

        # 6. Update Display
        pygame.display.update()

# =========================
# Execute
# ========================
intro_loop()
game_loop()
pygame.quit()
quit()