import pygame
import random
import math

# Pygame Setup
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Music and Sound Effects 
gameover_sound = pygame.mixer.Sound('gameOver.wav')
bubbles_sound = pygame.mixer.Sound('bubblessound.wav')
pygame.mixer.music.load('awake.wav')

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY_BLUE = (119, 182, 209)
WHITE_BLUE = (247, 253, 255)
HOVER_COLOR = (50, 70, 90)
TURQUOISE = (67, 240, 171)
PURPLE_BLUE = (111, 138, 176)

# Title and Icon
pygame.display.set_caption('Garbage Fisher')
icon = pygame.image.load('fishing-rod.png')
pygame.display.set_icon(icon)

# Fonts
font1 = pygame.font.SysFont ("segoeuiblack", 80)       # game menu title
font2 = pygame.font.SysFont ("freesansbold.ttf", 80)   # other titles
font3 = pygame.font.SysFont ("freesansbold.ttf", 50)   # mainly used for buttons
font4 = pygame.font.SysFont ("freesansbold.ttf", 30)   # used for text
font5 = pygame.font.SysFont ("freesansbold.ttf", 20)   # used for text

"""Texts"""
# for Game Menu
text_title = font1.render("Garbage Fisher", 1, HOVER_COLOR)
text_play = font3.render("Play", 1, WHITE)
text_instructions = font3.render("Instructions", 1, WHITE)
text_settings = font3.render("Settings", 1, WHITE)
text_exit = font3.render("Exit", 1, WHITE)

# for Game Over Menu
text_gameovertitle = font2.render("Game Over", 1, WHITE)
text_gameoverreplay = font3.render("Replay", 1, WHITE)
text_gameovermenu = font3.render("Menu", 1, WHITE)
text_gameoverexit = font3.render("Exit", 1, WHITE)

# for Instructions Page
text_instructtitle = font3.render("Instructions", 1, WHITE)
text_instructexit = font4.render("Exit", 1, WHITE)

# for the In-Game Exit Button
text_exitGame  = font4.render("Exit", 1,WHITE)

"""Rectangle Shapes For Buttons"""
# for Game Menu
rect_title = pygame.Rect(100, 80, 400, 80)
rect_play = pygame.Rect(250,200,300,60)
rect_instructions = pygame.Rect(250,300,300,60)
rect_exit = pygame.Rect(250, 400, 300, 60)

# for Game Over Menu
rect_gameovertitle = pygame.Rect(300, 100, 400, 80)
rect_gameoverscore = pygame.Rect(210,200,400,60)
rect_gameoverreplay = pygame.Rect(50,400,200,100)
rect_gameovermenu = pygame.Rect(300,400,200,100)
rect_gameoverexit = pygame.Rect(550,400,200,100)

# for Instructions Page
rect_instructtitle = pygame.Rect(300, 75, 400, 80)
rect_instructexit = pygame.Rect(350, 525, 100, 40)

# for the In-Game Exit Button
rect_exitGame  = pygame.Rect(670, 20, 80, 35)

"""Buttons"""
# for Game Menu
buttons_menu = [
    [text_play, rect_play, TURQUOISE],
    [text_instructions, rect_instructions, TURQUOISE],
    [text_exit, rect_exit, TURQUOISE]]

# for Game Over Menu
buttons_gameover = [
    [text_gameoverreplay, rect_gameoverreplay, BLACK],
    [text_gameovermenu, rect_gameovermenu, BLACK],
    [text_gameoverexit, rect_gameoverexit, BLACK]]

# for Instructions Page
button_instructexit = [text_instructexit, rect_instructexit, GREY_BLUE]

# for In-Game Exit Button
button_exitGame  = [text_exitGame , rect_exitGame , GREY_BLUE]

"""Info for Moving Graphics"""
# Boat
BOAT_SIZE = 80
boat_pos = [WIDTH/2, HEIGHT - 500]
boat_direction = "RIGHT"

# Plastic Bag
BAG_SIZE = 40
bag_pos = [WIDTH - BAG_SIZE, random.randint(HEIGHT - 450, HEIGHT - BAG_SIZE)]
bag_list = [bag_pos]

# Bottle
BOTTLE_SIZE = 40
bottle_pos_y_initial = random.randint(HEIGHT - 450, HEIGHT - BOTTLE_SIZE)
bottle_pos_y = bottle_pos_y_initial
bottle_pos = [WIDTH - BOTTLE_SIZE, bottle_pos_y, bottle_pos_y_initial]
bottle_list = [bottle_pos]

# E-Waste: Computer
COMP_SIZE = 45
comp_pos = [0 + COMP_SIZE, random.randint(HEIGHT - 450, HEIGHT - COMP_SIZE)]
comp_list = [comp_pos]

# E-Waste: Battery
BATTERY_SIZE = 32
battery_pos = [0 + BATTERY_SIZE, random.randint(HEIGHT - 450, HEIGHT - BATTERY_SIZE)]
battery_list = [battery_pos]

# Sea Life: Turtle
TURTLE_SIZE = 50
turtle_pos_y_initial = random.randint(HEIGHT - 450, HEIGHT - TURTLE_SIZE)
turtle_pos_y = turtle_pos_y_initial
turtle_pos = [0 + TURTLE_SIZE, turtle_pos_y, turtle_pos_y_initial]
turtle_list = [turtle_pos]

# Sea Life: Fish
FISH_SIZE = 40
fish_pos_y_initial = random.randint(HEIGHT - 450, HEIGHT - FISH_SIZE)
fish_pos_y = fish_pos_y_initial
fish_pos =  [0 + FISH_SIZE, fish_pos_y, fish_pos_y_initial]   
fish_list = [fish_pos]

# Sea Life: Jellyfish
JELLYFISH_SIZE = 40
jellyfish_pos = [0 + JELLYFISH_SIZE, random.randint(HEIGHT - 450, HEIGHT - JELLYFISH_SIZE)]
jellyfish_list = [jellyfish_pos]

# Bubble
BUBBLE_SIZE = 10
BUBBLE_RADIUS = 5
bubble_pos = [random.randint(0 + BUBBLE_SIZE, WIDTH - BUBBLE_SIZE), HEIGHT - BUBBLE_SIZE]
bubble_list = [bubble_pos]

# Return value from playing game
REPLAY = 1
BACKTO_MENU = 2
EXIT = 0

# Score
score = 0
score_txtX = 10
score_txtY = 10

# Life
life = 3  # player begins the game with three lives
life_txtX= 10
life_txtY = 50

# Determines speed of the game
def set_speed(score, speed):
    # Speed starts at 2
    speed = 2
    
    # Everytime the score increases by 10, the speed increases by two
    # If the score is >= 40, then the speed will remain at 12
    if score < 10:
        speed = 4
    elif score < 20:
        speed = 6
    elif score < 30:
        speed = 8
    elif score < 40:
        speed = 10
    else:
        speed = 12
        
    return speed

# Drops bubbles onto screen
def drop_bubble(bubble_list):
    # Delay to randomize when bubbles are added
    delay = random.random()
    # If there are less than 20 bubbles on the screen and the delay is less than 0.1, drop a new bubble
    if len(bubble_list) < 20 and delay < 0.1:
        x_pos = random.randint(0 + BUBBLE_SIZE, WIDTH - BUBBLE_SIZE)
        y_pos = HEIGHT - BUBBLE_SIZE
        bubble_list.append([x_pos, y_pos])     

# Draws bubbles
def draw_bubble(bubble_list):
    # For every bubble_pos in the bubble_list (x and y value of one bubble)
    # Draw a bubble based on its position 
    for bubble_pos in bubble_list:
        pygame.draw.circle(screen, GREY_BLUE , (bubble_pos[0] + BUBBLE_RADIUS, bubble_pos[1]), BUBBLE_RADIUS, 0)
        pygame.draw.circle(screen, WHITE_BLUE , (bubble_pos[0] + BUBBLE_RADIUS, bubble_pos[1]), BUBBLE_RADIUS, 1)

# Update bubble positions (movement and removal)
def update_bubble_positions(bubble_list):  
    for idxbubble, bubble_pos in enumerate(bubble_list):
        # If the y value of the bubble is greater than or equal to 160 
        # and the y value is smaller than the height of the screen
        # subtract 10 from the y value (moves the bubble upwards)
        if bubble_pos[1] >= 160 and bubble_pos[1] < HEIGHT:
            bubble_pos[1] -= 10
        
        # else remove the bubble
        else:
            bubble_list.pop(idxbubble)  

# Function to draw the game background
def draw_background():
    # Load background image and blit on screen
    backgroundImg = pygame.image.load('ocean-background.jpg')
    screen.blit(backgroundImg, (0,0))
    # Add moving bubbles in background
    drop_bubble(bubble_list)
    draw_bubble(bubble_list)
    update_bubble_positions(bubble_list)        

# Function to draw the boat
def drawboat(boat_pos, boat_direction):
    # If the boat is facing right direction
    if boat_direction == "RIGHT":    
        X = boat_pos[0]
        Y = boat_pos[1]
        boat_width = 100
        boat_height = 75
 
        """Top"""
        # First piece
        t1_X = X + 20
        t1_Y = Y
        t1_width = 12
        t1_height = 5
       
        #Second piece
        t2_X = X + 20
        t2_Y = Y + 5 #Y + t1_height
        t2_width = 12
        t2_height = 10
       
        #Third piece
        t3_X = X + 17
        t3_Y = Y + 5 + 10
        t3_width = 35
        t3_height = 5
       
        # Fourth piece
        t4_X = X + 17
        t4_Y = Y + 5 + 10 + 5
        t4_width = 30
        t4_height = 25
   
        # Fifth piece
        t5_X = X + 17
        t5_Y = Y + 5 + 10 + 5 + 5
        t5_width = 30
        t5_height = 15
       
        """Windows"""
        window_width = 8
        window_height = 5
        w1_X = X + 17
        w1_Y = Y + 5 + 10 + 5 + 5 + 5
        w2_X = X + 17 + window_width + 3
        w2_Y = Y + 5 + 10 + 5 + 5 + 5
        w3_X = X + 17 + 2*(window_width + 3)
        w3_Y = Y + 5 + 10 + 5 + 5 + 5
       
        """Bottom"""
        bottom_width = 80
        bottom_height = 30
        b_X1 = X
        b_Y1 = Y + 45
        b_X2 = X + 5
        b_Y2 = Y + 45 + bottom_height
        b_X3 = X + 5 + bottom_width
        b_Y3 = Y + 45 + bottom_height
        b_X4 = X + boat_width
        b_Y4 = Y + 45 - 10
        b_X5 = X + boat_width - 10
        b_Y5 = Y + 45 - 10
        b_X6 = X + 17 + 30
        b_Y6 = Y + 45
       
        # Top
        pygame.draw.rect(screen, BLACK, (t1_X, t1_Y, t1_width, t1_height), 0)
        pygame.draw.rect(screen, WHITE, (t2_X, t2_Y, t2_width, t2_height), 0)
        pygame.draw.rect(screen, BLACK, (t3_X, t3_Y, t3_width, t3_height), 0)
        pygame.draw.rect(screen, WHITE, (t4_X, t4_Y, t4_width, t4_height), 0)
        pygame.draw.rect(screen, RED, (t5_X, t5_Y, t5_width, t5_height), 0)
       
        # Windows
        pygame.draw.rect(screen, BLUE, (w1_X, w1_Y, window_width, window_height), 0)
        pygame.draw.rect(screen, BLUE, (w2_X, w2_Y, window_width, window_height), 0)
        pygame.draw.rect(screen, BLUE, (w3_X, w3_Y, window_width, window_height), 0)
       
        # Bottom
        pygame.draw.polygon(screen, RED, ((b_X1, b_Y1), (b_X2, b_Y2), (b_X3, b_Y3), (b_X4, b_Y4), (b_X5, b_Y5), (b_X6, b_Y6)), 0)
        pygame.draw.line(screen, WHITE, (b_X1 + 1, b_Y1 + 10), (b_X6, b_Y1 + 10), 3)
        pygame.draw.line(screen, WHITE, (b_X6, b_Y1 + 10), (b_X4 - 2, b_Y4 + 10), 3)
    
    # if the boat is facing the left direction 
    else:
        X = boat_pos[0]
        Y = boat_pos[1]
        boat_width = 100
        boat_height = 75
       
        """Top"""
        # First piece
        t1_width = 12
        t1_height = 5        
        t1_X = X + boat_width - 20 - t1_width
        t1_Y = Y
       
        #Second piece
        t2_width = 12
        t2_height = 10        
        t2_X = X + boat_width - 20 - t2_width
        t2_Y = Y + 5 #Y + t1_height
       
        #Third piece
        t3_width = 35
        t3_height = 5        
        t3_X = X + boat_width - 17 - t3_width
        t3_Y = Y + 5 + 10
       
        # Fourth piece
        t4_width = 30
        t4_height = 25        
        t4_X = X + boat_width - 17 - t4_width
        t4_Y = Y + 5 + 10 + 5
   
        # Fifth piece
        t5_width = 30
        t5_height = 15        
        t5_X = X + boat_width - 17 - t5_width
        t5_Y = Y + 5 + 10 + 5 + 5
             
        """Windows"""
        window_width = 8
        window_height = 5
        w1_X = X + boat_width - 17 - window_width
        w1_Y = Y + 5 + 10 + 5 + 5 + 5
        w2_X = X + boat_width - 17 - 3 - 2*window_width
        w2_Y = Y + 5 + 10 + 5 + 5 + 5
        w3_X = X + boat_width - 17 - (2*3) - (3*window_width)
        w3_Y = Y + 5 + 10 + 5 + 5 + 5
       
        """Bottom"""
        bottom_width = 80
        bottom_height = 30
        b_X1 = X
        b_Y1 = Y + 45 - 10
        b_X2 = X + 15
        b_Y2 = Y + 45 + bottom_height
        b_X3 = X + 15 + bottom_width
        b_Y3 = Y + 45 + bottom_height
        b_X4 = X + boat_width
        b_Y4 = Y + 45
        b_X5 = X + 53
        b_Y5 = Y + 45
        b_X6 = X + 10
        b_Y6 = Y + 45 - 10    
        
        # Top
        pygame.draw.rect(screen, BLACK, (t1_X, t1_Y, t1_width, t1_height), 0)
        pygame.draw.rect(screen, WHITE, (t2_X, t2_Y, t2_width, t2_height), 0)
        pygame.draw.rect(screen, BLACK, (t3_X, t3_Y, t3_width, t3_height), 0)
        pygame.draw.rect(screen, WHITE, (t4_X, t4_Y, t4_width, t4_height), 0)
        pygame.draw.rect(screen, RED, (t5_X, t5_Y, t5_width, t5_height), 0)
       
        # Windows
        pygame.draw.rect(screen, BLUE, (w1_X, w1_Y, window_width, window_height), 0)
        pygame.draw.rect(screen, BLUE, (w2_X, w2_Y, window_width, window_height), 0)
        pygame.draw.rect(screen, BLUE, (w3_X, w3_Y, window_width, window_height), 0)
       
        # Bottom
        pygame.draw.polygon(screen, RED, ((b_X1, b_Y1), (b_X2, b_Y2), (b_X3, b_Y3), (b_X4, b_Y4), (b_X5, b_Y5), (b_X6, b_Y6)), 0)
        pygame.draw.line(screen, WHITE, (b_X1 + 2, b_Y1 + 10), (b_X5, b_Y5 + 10), 3)
        pygame.draw.line(screen, WHITE, (b_X5, b_Y5 + 10), (b_X4 - 1, b_Y4 + 10), 3)

# Function to draw fishing rod
def drawfishingrod(boat_pos, boat_direction, y_string_end):  
    hook_width = 10
    hook_height = 10
    y_hook = y_string_end - 5
    y_rod_end = 40
    y_rod_start = 87
   
    # note the fishing rod is split into three parts (rod, hook, string)
   
    # if the boat is facing right
    if boat_direction == "RIGHT":
        # rod
        x_rod_start = boat_pos[0] + 80
        x_rod_end = x_rod_start + 40  
       
        # hook
        x_hook = x_rod_end - 10
    
    # if the boat is facing left
    else:
        # rod
        x_rod_start = boat_pos[0] + 20
        x_rod_end = x_rod_start - 40
               
        # hook
        x_hook = x_rod_end
   
    # string
    x_string = x_rod_end    
    y_string_start = y_rod_end

    # Draw the whole fishing rode
    pygame.draw.line(screen, BLACK, (x_rod_start,y_rod_start), (x_rod_end, y_rod_end), 4)      
    pygame.draw.line(screen, BLACK, (x_string, y_string_start), (x_string, y_string_end), 2)
    pygame.draw.arc(screen, BLACK, (x_hook, y_hook, hook_width, hook_height), math.pi, 2*math.pi, 2)

# Drops bottles onto screen    
def drop_bottle(bottle_list):
    # Delay to randomize when bottles are added
    delay = random.random()
    # if there are less than 6 bottles on the screen and 
    # the delay is less than 0.02, drop a new bottle
    if len(bottle_list) < 6 and delay < 0.02:
        x_pos = WIDTH - BOTTLE_SIZE
        # Set up initial y pos and a y pos (for parabola)
        y_pos_initial = random.randint(HEIGHT - 450, HEIGHT - BOTTLE_SIZE)
        y_pos = y_pos_initial
        bottle_list.append([x_pos, y_pos, y_pos_initial])     

# Drops bags onto screen    
def drop_bag(bag_list):
    # Delay to randomize when bags are added
    delay = random.random()
    # if there are less than 6 bags on the screen and 
    # the delay is less than 0.02, drop a new bag  
    if len(bag_list) < 6 and delay < 0.02:
        x_pos = WIDTH - BAG_SIZE
        y_pos = random.randint(HEIGHT - 450, HEIGHT - BAG_SIZE)
        bag_list.append([x_pos, y_pos])    

# Drops computers onto screen   
def drop_comp(comp_list):
    # Delay to randomize when computers are added
    delay = random.random()
    # if there are less than 2 computers on the screen and 
    # the delay is less than 0.02, drop a new computer       
    if len(comp_list) < 2 and delay < 0.01:
        x_pos = 0 + COMP_SIZE
        y_pos = random.randint(HEIGHT - 450, HEIGHT - COMP_SIZE)
        comp_list.append([x_pos, y_pos])  

# Drops batteries onto screen   
def drop_battery(battery_list):
    # Delay to randomize when batteries are added
    delay = random.random()
    # if there are less than 2 batteries on the screen and 
    # the delay is less than 0.01, drop a new batteries         
    if len(battery_list) < 2 and delay < 0.01:
        x_pos = 0 + BATTERY_SIZE
        y_pos = random.randint(HEIGHT - 450, HEIGHT - BATTERY_SIZE)
        battery_list.append([x_pos, y_pos])    

# Drops turtle onto screen
def drop_turtle(turtle_list):
    # delay to randomize when turtles are added
    delay = random.random()
    # if there is less than 1 turtle on the screen and 
    # the delay is less than 0.01, drop a new turtle        
    if len(turtle_list) < 1 and delay < 0.01:
        x_pos = 0 + TURTLE_SIZE
        # Set up initial y pos and second y pos (for parabola)
        y_pos_initial = random.randint(HEIGHT - 450, HEIGHT - TURTLE_SIZE)
        y_pos = y_pos_initial
        turtle_list.append([x_pos, y_pos, y_pos_initial])      

# Drops fish onto screen
def drop_fish(fish_list):
    # delay to randomize when fish are added 
    delay = random.random()
    # if there is less than 1 fish on the screen and 
    # the delay is less than 0.01, drop a new fish        
    if len(fish_list) < 1 and delay < 0.01:
        x_pos = 0 + FISH_SIZE
        # Set up initial y pos and a second y pos (for parabola)
        y_pos_initial = random.randint(HEIGHT - 450, HEIGHT - FISH_SIZE)
        y_pos = y_pos_initial
        fish_list.append([x_pos, y_pos, y_pos_initial])         

# Drops jellyfish onto screen
def drop_jellyfish(jellyfish_list):
    # delay to randomize when jellyfish are added 
    delay = random.random()    
    # if there is less than 1 jellyfish on the screen and 
    # the delay is less than 0.01, drop a new jellyfish          
    if len(jellyfish_list) < 1 and delay < 0.01:
        x_pos = 0 + JELLYFISH_SIZE
        y_pos = random.randint(HEIGHT - JELLYFISH_SIZE, HEIGHT - JELLYFISH_SIZE)
        jellyfish_list.append([x_pos, y_pos])          

# Draws all the garbage
def draw_garbage(bottle_list, bag_list, comp_list, battery_list):
    # For every " "_pos in the " "_list (x and y value of one garbage)
    # Draw a " " based on its position     
    # the " " represents the garbage
    for bottle_pos in bottle_list:
        bottleImg = pygame.image.load('plastic-bottle.png')  
        screen.blit(bottleImg, (bottle_pos[0], bottle_pos[1]))  
        
    for bag_pos in bag_list:
        bagImg = pygame.image.load('bag.png')  
        screen.blit(bagImg, (bag_pos[0], bag_pos[1]))  

    for comp_pos in comp_list:
        compImg = pygame.image.load('laptop2.png')
        screen.blit(compImg, (comp_pos[0], comp_pos[1]))
   
    for battery_pos in battery_list:
        batteryImg = pygame.image.load('battery.png')
        screen.blit(batteryImg, (battery_pos[0], battery_pos[1]))    

# Draws all the creatures      
def draw_creature(turtle_list, fish_list, jellyfish_list):
    # For every turtle_pos in the turtle_list (x and y value of one turtle)
    # Draw a turtle based on its position         
    for turtle_pos in turtle_list:
        # Overall turtle dimenshions
        X = turtle_pos[0]
        Y = turtle_pos[1]
        turtle_width = 53
        turtle_height = 45    
        
        # Shell dimenshions
        shell_width = 45
        shell_height = 25
        
        # Head dimenshions
        head_radius = 8
        headX = X + shell_width + head_radius//2
        headY = Y + head_radius      
        
        # Eye dimenshions
        eyeX = headX
        eyeY = headY - 2
        eye_radius = 2
        
        # Left leg dimenshions
        left_legX1 = X + 5
        left_legY1 = Y + shell_height - 5
        left_legX2 = X
        left_legY2 = Y + shell_height
        left_legX3 = X + 8
        left_legY3 = Y + shell_height + 2
        left_legX4 = X + 10
        left_legY4 = Y + shell_height - 5
        left_legX5 = X
        left_legY5 = Y + shell_height
        left_legX6 = X + 3
        left_legY6 = Y + shell_height + 5
        left_legX7 = X + 8
        left_legY7 = Y + shell_height + 2
       
        # Right leg dimenshions
        right_legX1 = X + shell_width - 15
        right_legY1 = Y + shell_height - 5
        right_legX2 = X + shell_width - 17
        right_legY2 = Y + shell_height
        right_legX3 = X + shell_width - 22
        right_legY3 = Y + shell_height + 5
        right_legX4 = X + shell_width - 22
        right_legY4 = Y + shell_height + 20
        right_legX5 = X + shell_width - 10
        right_legY5 = Y + shell_height + 3
        right_legX6 = X + shell_width - 8
        right_legY6 = Y + shell_height - 5
        right_legX7 = X + shell_width - 10
        right_legY7 = Y + shell_height - 5
   
       
        """Draw Face"""
        # Head
        pygame.draw.circle(screen, (232, 178, 133), (headX, headY), head_radius, 0)
        # Eye
        pygame.draw.circle(screen, BLACK, (eyeX, eyeY), eye_radius, 0)
       
        """Draw Shell"""
        pygame.draw.ellipse(screen, (0, 255, 0),(X, Y, shell_width, shell_height), 0)
       
        """Draw Legs"""
        # Left Leg
        pygame.draw.polygon(screen, (232, 178, 133),((left_legX1, left_legY1), (left_legX2, left_legY2), (left_legX3, left_legY3), (left_legX4, left_legY4)), 0)
        pygame.draw.polygon(screen, (232, 178, 133), ((left_legX5, left_legY5), (left_legX6, left_legY6), (left_legX7, left_legY7)), 0)
       
        # Right Leg
        pygame.draw.polygon(screen, (232, 178, 133),((right_legX1, right_legY1), (right_legX2, right_legY2), (right_legX3, right_legY3), (right_legX4, right_legY4), (right_legX5, right_legY5), (right_legX6, right_legY6)), 0)
           
    # For every fish_pos in the fish_list (x and y value of one fish)
    # Draw a fish based on its position     
    for fish_pos in fish_list:
        # Overall fish dimenshions
        X = fish_pos[0]
        Y = fish_pos[1]
        fish_width = 45
        fish_height = 30
        
        # Tail dimenshions
        tail_width = 15
        tail_height = 20
        tail_X1 = X
        tail_Y1 = Y + 5
        tail_X2 = X + 5
        tail_Y2 = Y + 5 + tail_height/2
        tail_X3 = X
        tail_Y3 = Y + 5 + tail_height
        tail_X4 = X + tail_width
        tail_Y4 = Y + 5 + tail_height - 6
        tail_X5 = X + tail_width
        tail_Y5 = Y + 5 + 6        
        
        # Body dimenshions
        body_X = X + tail_width
        body_Y = Y
        body_width = fish_width - tail_width
        body_height = fish_height
       
        # Eye dimenshions
        eye_X = X + fish_width - 10
        eye_Y = Y + 10
        eye_radius = 2
       
        """Draw Tail"""
        pygame.draw.polygon(screen, (255, 48, 62), ((tail_X1, tail_Y1), (tail_X2, tail_Y2), (tail_X3, tail_Y3), (tail_X4, tail_Y4), (tail_X5, tail_Y5)), 0)
       
       
        """Draw Body"""
        pygame.draw.ellipse(screen, (255, 115, 105), (body_X, body_Y, body_width, body_height),0 )
       
        """Draw Eye"""
        pygame.draw.circle(screen, BLACK, (eye_X, eye_Y), eye_radius, 0)
    
    # For every jellyfish_pos in the jellyfish_list (x and y value of one jellyfish)
    # Draw a jellyfish based on its position        
    for jellyfish_pos in jellyfish_list:
        jellyfishImg = pygame.image.load('jellyfish.png')
        screen.blit(jellyfishImg, (jellyfish_pos[0], jellyfish_pos[1]))    

# Updates garbage positions (movement and removal)
def update_garbage_positions(bottle_list, bag_list, comp_list, battery_list, score, speed):
    for idxbottle, bottle_pos in enumerate(bottle_list):
        # if the x value of the bottle is less than or equal to 0
        # and the x value is smaller than the width of the screen
        # subtract the speed from the x value (moves the bottle to left)
        # the y value will be calculated by sin function of x value
        if bottle_pos[0] >= 0 and bottle_pos[0] < WIDTH:
            bottle_pos[0] -= speed
            # the y value will be calculated by sin function of x value
            bottle_pos[1] = bottle_pos[2] + int(math.sin(bottle_pos[0]/30) * 20)
        
        # removes the bottle
        else:
            bottle_list.pop(idxbottle)

    # if the x value of the bag is less than or equal to 0 
    # and the x value is smaller than the width of the screen
    # subtract the speed from the x value (moves the bottle to the left)
    for idxbag, bag_pos in enumerate(bag_list):
        if bag_pos[0] >= 0 and bag_pos[0] < WIDTH:
            bag_pos[0] -= speed
        
        # removes the bag
        else:
            bag_list.pop(idxbag)
    
    # if the x value of the computer is less than or equal to 0
    # and the x value is smaller than the width of the screen
    # add the 2.5 times of the speed to the x value (moves the computer to the right)
    for idxcomp, comp_pos in enumerate(comp_list):
        if comp_pos[0] >= 0 and comp_pos[0] < WIDTH:
            comp_pos[0] += speed *2.5
        
        # remove computer
        else:
            comp_list.pop(idxcomp)
    
    # if the x value of the battery is less than or equal to 0
    # and the x value is smaller than the width of the screen
    # add the 3 times of the speed to the x value (moves the battery to the right)   
    for idxbattery, battery_pos in enumerate(battery_list):
        if battery_pos[0] >= 0 and battery_pos[0] < WIDTH:
            battery_pos[0] += speed *3
        else:
            battery_list.pop(idxbattery)    
   
# Updates creature positions (movement and removal)
def update_creature_positions(turtle_list, fish_list, jellyfish_list, score, speed):
    for idxturtle, turtle_pos in enumerate(turtle_list):
        # if the x value of the turtle is less than or equal to 0
        # and the x value is smaller than the width of the screen
        # add the speed to the x value (moves the turtle to the right)         
        if turtle_pos[0] >= 0 and turtle_pos[0] < WIDTH:
            turtle_pos[0] += speed
            #the y value will be calculated by sin function of x value
            turtle_pos[1] = turtle_pos[2] + int(math.sin(turtle_pos[0]/30) * 20)            
        
        # remove turtle
        else:
            turtle_list.pop(idxturtle)
                
    for idxfish, fish_pos in enumerate(fish_list):
        # if the x value of the fish is less than or equal to 0
        # and the x value is smaller than the width of the screen
        # add the speed to the x value (moves the fish to the right)          
        if fish_pos[0] >= 0 and fish_pos[0] < WIDTH:
            fish_pos[0] += speed
            #the y value will be calculated by sin function of x value
            fish_pos[1] = fish_pos[2] + int(math.sin(fish_pos[0]/30) * 20)
        
        # remove turtle     
        else:
            fish_list.pop(idxfish)
               
    for idxjellyfish, jellyfish_pos in enumerate(jellyfish_list):
        # if the x value of the jellyfish is less than or equal to 0
        # and the x value is smaller than the width of the screen
        # add the speed to the x value (moves the jellyfish to the right)          
        if jellyfish_pos[0] >= 0 and jellyfish_pos[0] < WIDTH:
            jellyfish_pos[0] += speed
        
        # remove jellyfish
        else:
            jellyfish_list.pop(idxjellyfish)    

# Determines garbage collision with fishing rod hook                 
def garbage_collision(boat_direction, bottle_list, bag_list, comp_list, battery_list, x_string, y_string_end, score): 
    x_hook = x_string - 10
    y_hook = y_string_end - 5
    
    # if the boat is facing right
    if boat_direction == "RIGHT":
        x_hook = x_string - 10
    # if the boat is facing left
    else:
        x_hook = x_string
        y_hook = y_string_end - 5
    
    # sets up the hook in a rectangle
    hook_width = 10
    hook_height = 10    
    hook_rect = pygame.Rect(x_hook, y_hook, hook_width, hook_height)
    
    for idxbottle, bottle_pos in enumerate(bottle_list):
        # sets up the bottle in a rectangle
        bottle_rect = pygame.Rect(bottle_pos[0], bottle_pos[1], BOTTLE_SIZE, BOTTLE_SIZE)
        # if the bottle collides with the hook, add 1 to the score
        if bottle_rect.colliderect(hook_rect):                
            bottle_list.pop(idxbottle)
            score += 1
   
    for idxbag, bag_pos in enumerate(bag_list):
        # sets up the bag in a rectangle
        bag_rect = pygame.Rect(bag_pos[0], bag_pos[1], BAG_SIZE, BAG_SIZE)  
        # if the bag collides with the hook, add 2 to the score
        if bag_rect.colliderect(hook_rect):                
            bag_list.pop(idxbag)
            score += 2
   
    for idxcomp, comp_pos in enumerate(comp_list):
        # sets up computer in a rectangle
        comp_rect = pygame.Rect(comp_pos[0], comp_pos[1], COMP_SIZE, COMP_SIZE)
        # if the computer collides with the hook, add 4 to the score
        if comp_rect.colliderect(hook_rect):
            comp_list.pop(idxcomp)
            score += 4
   
    for idxbattery, battery_pos in enumerate(battery_list):
        # sets up battery in a rectangle
        battery_rect = pygame.Rect(battery_pos[0], battery_pos[1], BATTERY_SIZE, BATTERY_SIZE)
        # if the batter collides with the hook, add 5 to the score
        if battery_rect.colliderect(hook_rect):
            battery_list.pop(idxbattery)
            score += 5  
    
    # returns updated score   
    return score

# Detects creature collision with fishing rod hook
def creature_collision(boat_direction, turtle_list, fish_list, jellyfish_list, x_string, y_string_end, life):
    x_hook = x_string - 10
    y_hook = y_string_end - 5    
    
    # if boat is facing right
    if boat_direction == "RIGHT":
        x_hook = x_string - 10
    # if boat is facing left
    else:
        x_hook = x_string
        y_hook = y_string_end - 5
    
    # set up hook in a rectangle
    hook_width = 10
    hook_height = 10    
    hook_rect = pygame.Rect(x_hook, y_hook, hook_width, hook_height)
    
    for idxturtle, turtle_pos in enumerate(turtle_list): 
        # set up turtle in a rectangle
        turtle_width = 53
        turtle_height = 45
        turtle_rect = pygame.Rect(turtle_pos[0], turtle_pos[1], turtle_width, turtle_height)  
        # if turtle collides with hook, remove a life
        if turtle_rect.colliderect(hook_rect):                
            turtle_list.pop(idxturtle)
            life -= 1
           
    for idxfish, fish_pos in enumerate(fish_list):    
        # set up fish in a rectangle
        fish_width = 45
        fish_height = 30        
        fish_rect = pygame.Rect(fish_pos[0], fish_pos[1], fish_width, fish_height)  
        # if fish collides with hook, remove a life  
        if fish_rect.colliderect(hook_rect):                
            fish_list.pop(idxfish)
            life -= 1    
           
    for idxjellyfish, jellyfish_pos in enumerate(jellyfish_list):
        # set up jellyfish in a rectangle
        jellyfish_rect = pygame.Rect(jellyfish_pos[0], jellyfish_pos[1], JELLYFISH_SIZE, JELLYFISH_SIZE)  
        # if jellyfish collides with hool, remove a life  
        if jellyfish_rect.colliderect(hook_rect):                
            jellyfish_list.pop(idxjellyfish)
            life -= 1    
    
    # return the updated life        
    return life

# Display score on screen
def show_score(x, y, score):
    score_txt = font3.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_txt, (x, y))

# Display life on screen   
def show_life(x, y, life):
    life_txt = font3.render("Life :", True, (255, 255, 255))
    screen.blit(life_txt, (x, y))
    heartImg = pygame.image.load('heart.png')
    
    # if life is 3, blit 3 hearts
    if life == 3:
        screen.blit(heartImg, (x + 100, y+5))
        screen.blit(heartImg, (x + 140, y+5))
        screen.blit(heartImg, (x + 180, y+5))
    
    # if life is 2, blit 2 hearts
    elif life == 2:
        screen.blit(heartImg, (x + 100, y+5))
        screen.blit(heartImg, (x + 140, y+5))     
    
    # if life is 1, blit 1 heart
    elif life == 1:
        screen.blit(heartImg, (x + 100, y+5))

# Funtion to draw menu
def drawMenu():
    # Play bubble sound effect
    pygame.mixer.Sound.play(bubbles_sound)
    
    # Menu loop runs while the running = True
    running = True
    while running:
        # Gets event
        for event in pygame.event.get():
            # if event type is pygame.QUIT, stop the loop
            if event.type == pygame.QUIT:
                running = False
            # if event is keydown
            elif event.type == pygame.KEYDOWN:
                # if esc key is pressed, stop the loop
                if event.key == pygame.K_ESCAPE:
                    running = False                
            
            # if event is mousemotion
            elif event.type == pygame.MOUSEMOTION:
                # determines if the mouse collides with the button
                for button in buttons_menu:
                    if button[1].collidepoint(event.pos):
                        # adds hover color if mouse is on top of button
                        button[2] = HOVER_COLOR
                    else:
                        # else, change color of button back to original color
                        button[2] = TURQUOISE
           # if event is mousebuttondown
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if user clicks the play button
                if rect_play.collidepoint(event.pos):
                    # stop the button sound
                    pygame.mixer.Sound.stop(bubbles_sound)
                    ret_value = REPLAY
                    # run the game_main function
                    while ret_value == REPLAY:
                        # set ret_value as the main game function
                        ret_value = game_main()
                
                # if the instructions button is clicked    
                elif rect_instructions.collidepoint(event.pos):
                    # run the instructions function
                    instructions()               
                
                # if the exit button is clicked 
                elif rect_exit.collidepoint(event.pos):
                    # break out of the loop
                    running = False
        
        # Background             
        draw_background()
        menuImg = pygame.image.load('plastic.png')
        screen.blit(menuImg, (0, 200))
        rodImg = pygame.image.load('rod.png')
        screen.blit(rodImg, (400, 200))
           
        # Title
        screen.blit(text_title, rect_title)              
        
        # Draws buttons
        for text, rect, color in buttons_menu:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, (rect.x, rect.y+15))

        pygame.display.flip()
        clock.tick(20)

# Function for instructions page        
def instructions():        
    running = True
    while running:
        # get events
        for event in pygame.event.get():
            # if user tries to close the window, stop the loop
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                # if user presses esc key, stop the loop
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
            elif event.type == pygame.MOUSEMOTION:
                    # if mouse is on exit button
                    if button_instructexit[1].collidepoint(event.pos):
                        # change button color
                        button_instructexit[2] = HOVER_COLOR
                    else:
                        # otherwise change button color back to original color
                        button_instructexit[2] = GREY_BLUE
            
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                # if exit button is clicked, stop the loop
                if rect_instructexit.collidepoint(event.pos):
                    running = False            
            
        # Background
        draw_background()
        pygame.draw.rect(screen, GREY_BLUE, (50, 50, 700, 450), 0)
        pygame.draw.rect(screen, WHITE_BLUE, (50, 50, 700, 450), 3)
        
        # Title
        screen.blit(text_instructtitle, rect_instructtitle)
        
        # Objective Paragraph
        rect_objective1 = pygame.Rect(60, 120, 680, 25)
        rect_objective2 = pygame.Rect(60, 145, 680, 25)
        rect_objective3 = pygame.Rect(60, 170, 680, 25)
        text_objective1 = font5.render("      Time to save our oceans! E-waste in oceans affects marine wildlife and are contained of", 1, BLACK)
        text_objective2 = font5.render("toxic chemicals that contaminate the waters. The garbage in the oceans can kill sea creatures", 1, BLACK)
        text_objective3 = font5.render("and pollute the waters. Today you will be fishing for garbage instead of fish!", 1, BLACK)
        screen.blit(text_objective1, rect_objective1)
        screen.blit(text_objective2, rect_objective2)
        screen.blit(text_objective3, rect_objective3)               
               
        # What to do
        rect_what1 = pygame.Rect(60, 200, 250, 30)
        rect_what2 = pygame.Rect(60, 225, 250, 30)
        text_what1 = font4.render("   Fish garbage and ", 1, WHITE_BLUE)
        text_what2 = font4.render("e-waste to earn points", 1, WHITE_BLUE)
        screen.blit(text_what1, rect_what1)
        screen.blit(text_what2, rect_what2)
        
        bottleImg = pygame.image.load('plastic-bottle.png')  
        screen.blit(bottleImg, (60, 260))  
        rect_what3 = pygame.Rect(70, 310, 60, 20)
        text_what3 = font5.render("1 pt", 1, WHITE_BLUE)
        screen.blit(text_what3, rect_what3)   
        
        bagImg = pygame.image.load('bag.png')  
        screen.blit(bagImg, (130, 260))
        rect_what4 = pygame.Rect(135, 310, 60, 20)
        text_what4 = font5.render("2 pts", 1, WHITE_BLUE)
        screen.blit(text_what4, rect_what4)        
        
        compImg = pygame.image.load('laptop2.png')
        screen.blit(compImg, (200, 260))
        rect_what5 = pygame.Rect(205, 310, 60, 20)
        text_what5 = font5.render("4 pts", 1, WHITE_BLUE)
        screen.blit(text_what5, rect_what5)
        
        batteryImg = pygame.image.load('battery.png')
        screen.blit(batteryImg, (270, 260))
        rect_what6 = pygame.Rect(270, 310, 60, 20)
        text_what6 = font5.render("5 pts", 1, WHITE_BLUE)
        screen.blit(text_what6, rect_what6)  
        
        # Dont do
        rect_dont1 = pygame.Rect(350, 200, 250, 30)
        text_dont1 = font4.render("   You have three lives: ", 1, WHITE_BLUE)
        screen.blit(text_dont1, rect_dont1)
        lifeImg = pygame.image.load('heart.png')
        screen.blit(lifeImg, (585, 200))
        screen.blit(lifeImg, (625, 200))
        screen.blit(lifeImg, (665, 200))
        
        rect_dont2 = pygame.Rect(400, 240, 250, 30)
        rect_dont3 = pygame.Rect(430, 265, 250, 30)
        text_dont2 = font4.render("If you fish a sea creature,", 1, WHITE_BLUE)
        text_dont3 = font4.render("then you lose a life.", 1, WHITE_BLUE)
        screen.blit(text_dont2, rect_dont2)
        screen.blit(text_dont3, rect_dont3)
        
        X = 400
        Y = 300
        turtle_width = 53
        turtle_height = 45       
        shell_width = 45
        shell_height = 25
        head_radius = 8
        headX = X + shell_width + head_radius//2
        headY = Y + head_radius      
        eyeX = headX
        eyeY = headY - 2
        eye_radius = 2
        left_legX1 = X + 5
        left_legY1 = Y + shell_height - 5
        left_legX2 = X
        left_legY2 = Y + shell_height
        left_legX3 = X + 8
        left_legY3 = Y + shell_height + 2
        left_legX4 = X + 10
        left_legY4 = Y + shell_height - 5
        left_legX5 = X
        left_legY5 = Y + shell_height
        left_legX6 = X + 3
        left_legY6 = Y + shell_height + 5
        left_legX7 = X + 8
        left_legY7 = Y + shell_height + 2
        right_legX1 = X + shell_width - 15
        right_legY1 = Y + shell_height - 5
        right_legX2 = X + shell_width - 17
        right_legY2 = Y + shell_height
        right_legX3 = X + shell_width - 22
        right_legY3 = Y + shell_height + 5
        right_legX4 = X + shell_width - 22
        right_legY4 = Y + shell_height + 20
        right_legX5 = X + shell_width - 10
        right_legY5 = Y + shell_height + 3
        right_legX6 = X + shell_width - 8
        right_legY6 = Y + shell_height - 5
        right_legX7 = X + shell_width - 10
        right_legY7 = Y + shell_height - 5
        pygame.draw.circle(screen, (232, 178, 133), (headX, headY), head_radius, 0)
        pygame.draw.circle(screen, BLACK, (eyeX, eyeY), eye_radius, 0)
        pygame.draw.ellipse(screen, (0, 255, 0),(X, Y, shell_width, shell_height), 0)
        pygame.draw.polygon(screen, (232, 178, 133),((left_legX1, left_legY1), (left_legX2, left_legY2), (left_legX3, left_legY3), (left_legX4, left_legY4)), 0)
        pygame.draw.polygon(screen, (232, 178, 133), ((left_legX5, left_legY5), (left_legX6, left_legY6), (left_legX7, left_legY7)), 0)
        pygame.draw.polygon(screen, (232, 178, 133),((right_legX1, right_legY1), (right_legX2, right_legY2), (right_legX3, right_legY3), (right_legX4, right_legY4), (right_legX5, right_legY5), (right_legX6, right_legY6)), 0)        
        
        X = 480
        Y = 300
        fish_width = 45
        fish_height = 30
        tail_width = 15
        tail_height = 20
        tail_X1 = X
        tail_Y1 = Y + 5
        tail_X2 = X + 5
        tail_Y2 = Y + 5 + tail_height/2
        tail_X3 = X
        tail_Y3 = Y + 5 + tail_height
        tail_X4 = X + tail_width
        tail_Y4 = Y + 5 + tail_height - 6
        tail_X5 = X + tail_width
        tail_Y5 = Y + 5 + 6        
        body_X = X + tail_width
        body_Y = Y
        body_width = fish_width - tail_width
        body_height = fish_height
        eye_X = X + fish_width - 10
        eye_Y = Y + 10
        eye_radius = 2
        pygame.draw.polygon(screen, (255, 48, 62), ((tail_X1, tail_Y1), (tail_X2, tail_Y2), (tail_X3, tail_Y3), (tail_X4, tail_Y4), (tail_X5, tail_Y5)), 0)
        pygame.draw.ellipse(screen, (255, 115, 105), (body_X, body_Y, body_width, body_height),0 )    
        pygame.draw.circle(screen, BLACK, (eye_X, eye_Y), eye_radius, 0)
        
        jellyfishImg = pygame.image.load('jellyfish.png')
        screen.blit(jellyfishImg, (560, 300))
        
        # Key Controls
        keyboardImg = pygame.image.load('keyboard.png')
        screen.blit(keyboardImg, (80, 370))
        
        rect_key1 = pygame.Rect(170, 390, 200, 20)
        text_key1 = font4.render("Up and Down keys", 1, WHITE_BLUE)
        screen.blit(text_key1, rect_key1)
        rect_key2 = pygame.Rect(170, 415, 230, 20)
        text_key2 = font4.render("to control fishing rod", 1, WHITE_BLUE)
        screen.blit(text_key2, rect_key2)
        
        rect_key3 = pygame.Rect(100, 450, 200, 20)
        text_key3 = font4.render("Left and Right keys to control boat", 1, WHITE_BLUE)
        screen.blit(text_key3, rect_key3)
        
        # Enjoy
        personImg = pygame.image.load('person.png')
        screen.blit(personImg, (500, 370))
        rect_enjoy = pygame.Rect(610, 410, 100, 40)
        text_enjoy = font3.render("ENJOY!", 1, WHITE_BLUE)
        screen.blit(text_enjoy, rect_enjoy)
    
        # Exit Button
        pygame.draw.rect(screen, button_instructexit[2], rect_instructexit)
        screen.blit(text_instructexit, rect_instructexit)            
        
        pygame.display.flip()
        clock.tick(20)    

# Game over menu
def drawGameOver(score):
    # Plays game over sound effect
    pygame.mixer.Sound.play(gameover_sound)
    ret_value = EXIT
    running = True
    while running:
        # get events
        for event in pygame.event.get():
            # if use tries to close window
            if event.type == pygame.QUIT:
                # stop game over sound effect and play bubbles sound effect and stop the loop
                pygame.mixer.Sound.stop(gameover_sound)
                pygame.mixer.Sound.play(bubbles_sound)
                running = False

            elif event.type == pygame.KEYDOWN:
                # if user presses esc key
                if event.key == pygame.K_ESCAPE:
                    # stop gameover sound, play bubbles sound, and stop the loop
                    pygame.mixer.Sound.stop(gameover_sound)
                    pygame.mixer.Sound.play(bubbles_sound)
                    running = False                
                    
            elif event.type == pygame.MOUSEMOTION:
                # if mouse is on a button
                for button in buttons_gameover:
                    if button[1].collidepoint(event.pos):
                        # change color of button
                        button[2] = HOVER_COLOR
                    else:
                        # otherwise reset the color of the button back to original color
                        button[2] = BLACK
           
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if user preses replay button
                if rect_gameoverreplay.collidepoint(event.pos):
                    # stop the game over sound and stop the loop
                    pygame.mixer.Sound.stop(gameover_sound)
                    
                    # Sets ret value as replay
                    ret_value = REPLAY
                    running = False
                # if user presses the menu button
                elif rect_gameovermenu.collidepoint(event.pos):
                    # stop the game over sound, play the bubbles sound, and stop the loop
                    pygame.mixer.Sound.stop(gameover_sound)
                    pygame.mixer.Sound.play(bubbles_sound)
                   
                    # Sets ret_value as BACKTO_MENU
                    ret_value = BACKTO_MENU
                    running = False
                
                # if user presses the exit button
                elif rect_gameoverexit.collidepoint(event.pos):
                    # stop the game over sound, play the bubbles sound, and stop the loop
                    pygame.mixer.Sound.stop(gameover_sound)
                    pygame.mixer.Sound.play(bubbles_sound)
            
                    # sets ret_value as EXIT
                    ret_value = EXIT
                    running = False
        
        # Background          
        screen.fill(PURPLE_BLUE)
        fishermanImg = pygame.image.load('fisherman.png')
        screen.blit(fishermanImg, (150, 50))

        # Title
        screen.blit(text_gameovertitle, rect_gameovertitle)   
        
        # Score
        text_gameoverscore = font2.render("Your Score is " + str(score), 1, BLACK)              
        screen.blit(text_gameoverscore, rect_gameoverscore)   
        
        # Text
        rect_text = pygame.Rect(200, 320, 200, 30)
        text_text = font4.render("That's what you get for fishing sea creatures!", 1, BLACK)
        screen.blit(text_text, rect_text)        

        # Draw Buttons
        for text, rect, color in buttons_gameover:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, (rect.x, rect.y+15))
            
        pygame.display.flip()
        clock.tick(5)
    
    return ret_value

# Main game function
def game_main():
    # Play music infinitly
    pygame.mixer.music.play(-1)
    
    # sets ret_value as EXIT
    ret_value = EXIT
    
    # Set score, speed, and life
    score = 0
    speed = 10
    life = 3
   
    # Boat Dimenshions
    boat_pos = [WIDTH/2, HEIGHT - 550]
    boat_width = 100
    boat_height = 75
    boat_direction = "RIGHT"
    
    # Fishing Rod dimenshions (string, hook, rod)
    y_string_end = 100
    x_string = 100
   
    hook_height = 10
   
    x_rod_start = boat_pos[0] + 80
    x_rod_end = x_rod_start + 40      
   
    # Set game_over as False
    game_over = False
   
    running = True
    while running:
        # get events
        for event in pygame.event.get():
            # if user tries to close the window
            if event.type == pygame.QUIT:
                # stop the music
                pygame.mixer.music.stop()
                # play bubbles sound
                pygame.mixer.Sound.play(bubbles_sound)
                # stop the loop
                running = False      
            elif event.type == pygame.MOUSEMOTION:
                # if mouse is on the exit button
                if rect_exitGame.collidepoint(event.pos):
                    # change the button color 
                    button_exitGame[2] = HOVER_COLOR
                else:
                    # otherwise reset the color back to original color
                    button_exitGame[2] = GREY_BLUE
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if user presses the exit button
                if rect_exitGame.collidepoint(event.pos):
                    # play the bubbles sound
                    pygame.mixer.Sound.play(bubbles_sound)
                    # stop the music
                    pygame.mixer.music.stop()
                    # stop the loop
                    running = False    
                    
            elif event.type == pygame.KEYDOWN:
                # boat dimenshions
                x_boat = boat_pos[0]
                y_boat = boat_pos[1]
           
                if event.key == pygame.K_ESCAPE:
                    # if user presses esc key, stop the music
                    pygame.mixer.music.stop()
                    # stop the loop
                    running = False

                elif event.key == pygame.K_RIGHT:
                    # if user presses right key, determine the boat dimenshions
                    x_boat += BOAT_SIZE
                    boat_direction = "RIGHT"

                elif event.key == pygame.K_LEFT:
                    # if user presses the left key, determine the boat dimenshions
                    x_boat -= BOAT_SIZE
                    boat_direction = "LEFT"
                
                # if user presses up key  
                elif event.key == pygame.K_UP:
                    # makes sure fishing rod does not go over boundaries
                    if y_string_end - 50 < 100:
                        # string stops at 100 and does not go any higher
                        y_string_end = 100
                   
                    else:
                        # else, the string subtracts 50 and moves up
                        y_string_end -= 50
                
                # if user presses down key
                elif event.key == pygame.K_DOWN:  
                    # makes sure fishing rod does not go over boundaries
                    if y_string_end + 50 > HEIGHT - hook_height:
                        # string stops at the height - hook_height and does not go any lower
                        y_string_end = HEIGHT - hook_height  
                       
                    else:
                        # otherwise add 50 and the string moves down
                        y_string_end += 50
                
                # sets boundaries for the boat
                if x_boat < 50:
                    x_boat = 50
                elif x_boat > 650:
                    x_boat = 650
                
                boat_pos = [x_boat,y_boat]
        
        # determines rod dimenshipons if the boat is facing right
        if boat_direction == "RIGHT":
            # rod
            x_rod_start = boat_pos[0] + 80
            x_rod_end = x_rod_start + 40    
        
        # determines rod dimenshipons if the boat is facing left
        else:
            # rod
            x_rod_start = boat_pos[0] + 20
            x_rod_end = x_rod_start - 40
                           
        # string
        x_string = x_rod_end  
        
        # Background
        draw_background()
       
        # Display score and life
        show_score(score_txtX, score_txtY, score)
        show_life(life_txtX, life_txtY, life)
        
        # Drop garbage and creatures
        drop_bottle(bottle_list)
        drop_bag(bag_list)
        drop_comp(comp_list)
        drop_battery(battery_list)
        drop_turtle(turtle_list)
        drop_fish(fish_list)
        drop_jellyfish(jellyfish_list)
        
        # Update positions 
        update_garbage_positions(bottle_list, bag_list, comp_list, battery_list, score, speed)
        update_creature_positions(turtle_list, fish_list, jellyfish_list, score, speed)
        
        # Update Speed
        speed = set_speed(score, speed)
        
        # Draw images
        draw_garbage(bottle_list, bag_list, comp_list, battery_list)
        draw_creature(turtle_list, fish_list, jellyfish_list)
       
        drawboat(boat_pos, boat_direction)
        drawfishingrod(boat_pos, boat_direction, y_string_end)
        
        # Exit Button          
        pygame.draw.rect(screen, button_exitGame[2], rect_exitGame)
        screen.blit(text_exitGame, rect_exitGame)
    
        # Update score and life
        score = garbage_collision(boat_direction, bottle_list, bag_list, comp_list, battery_list, x_string, y_string_end, score)
        life = creature_collision(boat_direction, turtle_list, fish_list, jellyfish_list, x_string, y_string_end, life)
       
        # Check if game over
        if life <= 0:
            # stops the music
            pygame.mixer.music.stop()
            ret_value = drawGameOver(score)
            running = False
       
        pygame.display.flip()
        clock.tick(20)
       
    # Returns updated ret_value
    return ret_value


drawMenu()
pygame.quit() 
