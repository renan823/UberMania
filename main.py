import pygame
from move import *
from city import *
from mission import *

yellow = (255, 255, 0)
magenta = (255, 0, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)
width = 600
height = 600

actualScreen = "Start"

pygame.init()
screen  = pygame.display.set_mode((width, height))
pygame.display.set_caption("Uber mania")

def screenText(txt, pos, color, size):                              
    pygame.font.init()                                
    font = pygame.font.get_default_font()              
    useFont = pygame.font.SysFont(font , size)           
    txtScreen = useFont.render(txt, 1, color)  
    screen.blit(txtScreen, pos)       

def start():
    return {"x": width/2, "y": height/2 - 20, "w": 20, "h": 20, "v": 0.3, "direction": "R", "points": 0, "passenger": False}

car = start()
passenger = createPassenger(getBuilds(), width, height)
check = createCheckPoint(getBuilds(), width, height)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            #Directions
            if event.key == pygame.K_LEFT:
                car["direction"] = "L"
            if event.key == pygame.K_RIGHT:
                car["direction"] = "R"
            if event.key == pygame.K_UP:
                car["direction"] = "U"
            if event.key == pygame.K_DOWN:
                car["direction"] = "D"

            #Velocity
            if event.key == 49:
                car["v"] = 0.3
            if event.key == 50:
                car["v"] = 0.4
            if event.key == 51:
                car["v"] = 0.5
            if event.key == 52:
                car["v"] = 0.6

            #Restart
            if event.key == 114:
                car = start()
                passenger = createPassenger(getBuilds(), width, height)
                check = createCheckPoint(getBuilds(), width, height)

            #Start Game
            if event.key == 32:
                if(actualScreen == "Start"):
                    actualScreen = "Game"

    car = move(car, width, height)
    if collisionPassenger(car, passenger):
        car["passenger"] = True

    if collisionCheck(car, check):
        car["passenger"] = False
        car["points"] += 1
        passenger = createPassenger(getBuilds(), width, height)
        check = createCheckPoint(getBuilds(), width, height)
        
    screen.fill(black) 
    if actualScreen == "Game":
        #draw Map
        drawMap(pygame, screen)
        #draw CheckPoint
        pygame.draw.rect(screen, cyan, [check.get("x"), check.get("y"), check.get("w"), check.get("h")])
        pygame.draw.rect(screen, black, [check.get("x") + 3, check.get("y") + 3, check.get("w") - 6, check.get("h") - 6])
        pygame.draw.rect(screen, cyan, [check.get("x") + 6, check.get("y") + 6, check.get("w") - 12, check.get("h") - 12])
        #draw Car
        pygame.draw.rect(screen, yellow, [car.get("x"), car.get("y"), car.get("w"), car.get("h")])
    
        if collision(car):
            car["v"] = 0
            screenText('You crashed! "R" to restart!', (width/2 - 270, height/2 - 50), magenta, 60)

        #draw Passenger (if not in car)
        if not car.get("passenger"):
            pygame.draw.rect(screen, cyan, [passenger.get("x"), passenger.get("y"), passenger.get("w"), passenger.get("h")])
    
        #Write total points
        screenText(str(car.get("points")), (10, 10), magenta, 40)
    else:
        screenText('Uber Mania', (width/2 - 120, height/2 - 250), magenta, 60)
        screenText(' - Pick up passengers!', (width/2 - 220, height/2 - 150), magenta, 40)
        screenText(' - Run around town!', (width/2 - 220, height/2 - 120), magenta, 40)
        screenText(' - Collect points', (width/2 - 220, height/2 - 90), magenta, 40)
        screenText(' - Use 1 - 4 to change your speed!', (width/2 - 220, height/2 - 60), magenta, 40)
        screenText('Press "SpaceBar" to start!', (width/2 - 180, height/2), magenta, 40)

    pygame.display.update()