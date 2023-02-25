class inputReader:
    currInput = None
    buffer = None

    def readInput():
        buffer = input()
        currInput = buffer[-1]

    def interpretInput(player, currInput):
        if currInput == "w":
            updatePos(player, "w")
        if currInput == "a":
            updatePos(player, "a")
        if currInput == "s":
            updatePos(player, "s")
        if currInput == "d":
            updatePos(player, "d")