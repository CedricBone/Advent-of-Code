input = open("../inputs/input2.txt", "r")
gameID = 1
IDsum = 0


def parse(game):
    game = game[game.index(":") + 2 :]
    game = game.replace("; ", ", ")
    game = game.split(", ")
    return game


def isPossible(parameters, game):
    for index in range(len(game)):
        if ("red" in game[index]) and (parameters[0] < int(game[index].split(" ")[0])):
            return False
        elif ("green" in game[index]) and (
            parameters[1] < int(game[index].split(" ")[0])
        ):
            return False
        elif ("blue" in game[index]) and (
            parameters[2] < int(game[index].split(" ")[0])
        ):
            return False
    return True


for line in input:
    game = parse(line)
    parameters = [12, 13, 14]
    if isPossible(parameters, game):
        IDsum += gameID
    gameID += 1

print(f"The sum of all of the valid game IDs is {IDsum}")
