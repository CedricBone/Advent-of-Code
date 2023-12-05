input = open("../inputs/input2.txt", "r")
total = 0


def parse(game):
    game = game[game.index(":") + 2 :]
    game = game.replace("; ", ", ")
    game = game.split(", ")
    return game


def minGamePower(game):
    red = 0
    green = 0
    blue = 0
    for index in range(len(game)):
        value = int(game[index].split(" ")[0])
        if ("red" in game[index]) and (red < value):
            red = value
        elif ("green" in game[index]) and (green < value):
            green = value
        elif ("blue" in game[index]) and (blue < value):
            blue = value
    print(f"red: {red}, green: {green}, blue: {blue}")
    return red * green * blue


for line in input:
    game = parse(line)
    total += minGamePower(game)

print(f"The total game power is {total}")
