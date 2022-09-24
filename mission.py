import random

def inBuilds(builds, item):
    for build in builds:
        if build.get("x") < item.get("x") + item.get("w") and build.get("x") + build.get("w") > item.get("x") and build.get("y") < item.get("y") + item.get("h") and build.get("y") + build.get("h") > item.get("y") :
            return True
    return False       

def createPassenger(builds, width, height):
    passenger = {"x": 0, "y": 0, "w": 10, "h": 10}
    passenger["x"] = random.randint(0, width - passenger.get("w"))//10 * 10
    passenger["y"] = random.randint(0, height - passenger.get("h"))//10 * 10

    while(inBuilds(builds, passenger)):
        passenger["x"] = random.randint(0, width - passenger.get("w"))//10 * 10
        passenger["y"] = random.randint(0, height - passenger.get("h"))//10 * 10
    return passenger

def createCheckPoint(builds, width, height):
    check = {"x": 0, "y": 0, "w": 20, "h": 20}
    check["x"] = random.randint(0, width - check.get("w"))//10 * 10
    check["y"] = random.randint(0, height - check.get("h"))//10 * 10

    while(inBuilds(builds, check)):
        check["x"] = random.randint(0, width - check.get("w"))//10 * 10
        check["y"] = random.randint(0, height - check.get("h"))//10 * 10
    return check

def collisionPassenger(car, passenger):
    if car.get("x") < passenger.get("x") + passenger.get("w") and car.get("x") + car.get("w") > passenger.get("x") and car.get("y") < passenger.get("y") + passenger.get("h") and car.get("y") + car.get("h") > passenger.get("y") :
        return True
    return False

def collisionCheck(car, check):
    if car.get("passenger"):
        if car.get("x") < check.get("x") + check.get("w") and car.get("x") + car.get("w") > check.get("x") and car.get("y") < check.get("y") + check.get("h") and car.get("y") + car.get("h") > check.get("y") :
            return True
    return False