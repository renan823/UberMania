def move(car, width, height):
    if car.get("direction") == "L":
        if car.get("x") - car.get("v") <= 0:
            car["direction"] = "U"
        else:
            car["x"] -= car.get("v")

    if car.get("direction") == "R":
        if car.get("x") + car.get("v") + car.get("w")>= width:
            car["direction"] = "D"
        else:
            car["x"] += car.get("v")

    if car.get("direction") == "U":
        if car.get("y") - car.get("v") <= 0:
            car["direction"] = "R"
        else:
            car["y"] -= car.get("v")

    if car.get("direction") == "D":
        if car.get("y") + car.get("v") + car.get("h") >= height:
            car["direction"] = "L"
        else:
            car["y"] += car.get("v")

    return car