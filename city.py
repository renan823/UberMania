builds = [
    {"x": 40, "y": 40, "w": 165, "h": 230, "color": (255, 255, 255)}, 
    {"x": 40, "y": 310, "w": 165, "h": 130, "color": (255, 255, 255)}, 
    {"x": 40, "y": 480, "w": 165, "h": 80, "color": (255, 255, 255)},
    #nova coluna de construções
    {"x": 245, "y": 40, "w": 125, "h": 100, "color": (255, 255, 255)},
    {"x": 320, "y": 130, "w": 50, "h": 50, "color": (255, 255, 255)},
    {"x": 245, "y": 180, "w": 125, "h": 90, "color": (255, 255, 255)},
    {"x": 245, "y": 310, "w": 220, "h": 40, "color": (255, 255, 255)},
    {"x": 245, "y": 390, "w": 140, "h": 170, "color": (255, 255, 255)},
    {"x": 425, "y": 340, "w": 40, "h": 220, "color": (255, 255, 255)},
    #nova coluna de construções
    {"x": 410, "y": 40, "w": 145, "h": 120, "color": (255, 255, 255)},
    {"x": 410, "y": 200, "w": 145, "h": 70, "color": (255, 255, 255)},
    {"x": 505, "y": 310, "w": 50, "h": 250, "color": (255, 255, 255)},
]

def getBuilds():
    return builds

def collision(car):
    for build in builds:
        if build.get("x") < car.get("x") + car.get("w") and build.get("x") + build.get("w") > car.get("x") and build.get("y") < car.get("y") + car.get("h") and build.get("y") + build.get("h") > car.get("y") :
            return True
    return False

def drawMap(pygame, screen):
    for build in builds:
        pygame.draw.rect(screen, build.get("color"), [build.get("x"), build.get("y"), build.get("w"), build.get("h")])