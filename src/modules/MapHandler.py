from modules.GlobalConf import *
from random import randint, choice

class MapHandler():
    def __init__(self,  xSize=10, ySize=10, startingIndex=(0, 0)) -> None:
        self.map = []
        self.curUID = -1 # Used to set a unique id for each cell in the map.

        # Map generation related: quantity of columns and rows.
        self.xSize = xSize
        self.ySize = ySize

        # Used for the calculations of the player position
        self.currentCoords = startingIndex

        self.generate()
        self.__internalMove(self.currentCoords)

    # Used to generate unique UIDs for the cell locations
    def __generateUID(self):
        self.curUID += 1
        return self.curUID
    # Randomly generates the map array
    def generate(self):
        for i in range(self.ySize):
            self.map.append([])
            for j in range(self.xSize):
                rng = randint(0, 100)
                
                # Residential
                if rng < 60:
                    self.map[i].append(self.__generateLocation("Residential"))
                # Commercial
                if rng >= 60 and rng < 85:
                    self.map[i].append(self.__generateLocation("Commercial"))
                # Industrial
                if rng >= 85:
                    self.map[i].append(self.__generateLocation("Industrial"))
    # Used to generate random locations based on the category passed as argument
    def __generateLocation(self, category):
        uidGenerated = self.__generateUID()

        if category == "Residential":
            return Location(choice(MAP_RES_NAMES), uidGenerated, "Residential", MAP_RES_ICON)
        if category == "Commercial":
            return Location(choice(MAP_COM_NAMES), uidGenerated, "Commercial", MAP_COM_ICON)
        if category == "Industrial":
            return Location(choice(MAP_IND_NAMES), uidGenerated, "Industrial", MAP_IND_ICON)
    # Returns the current cell the player is on
    def __getCurrentCell(self):
        return self.map[self.currentCoords[0]][self.currentCoords[1]]
    # Used internally by other functions to move the player to the determined coords.
    def __internalMove(self, coords):
        self.__getCurrentCell().playerIsOn = False

        self.map[coords[0]][coords[1]].playerIsOn = True
        self.currentCoords = coords

    # Prints a human-readable map on the terminal
    def show(self):
        for i in range(self.ySize):
            for j in range(self.xSize):
                print(self.map[i][j].getIcon(), end=" ")
            print("\n")
        if DEBUG:
            print(self.__getCurrentCell().uid)
    # "Interfaces" the internal move function with the word system
    def move(self, direction):
        # Horizontal
        if direction == "right":
            if self.currentCoords[1] + 2 > len(self.map[self.currentCoords[0]]):
                return False
            else:
                self.__internalMove((self.currentCoords[0], self.currentCoords[1] + 1))
                return True
        elif direction == "left":
            if self.currentCoords[1] - 1 < 0:
                return False
            else:
                self.__internalMove((self.currentCoords[0], self.currentCoords[1] - 1))
                return True
        # Vertical
        elif direction == "up":
            if self.currentCoords[0] - 1 < 0:
                return False
            else:
                self.__internalMove((self.currentCoords[0] - 1, self.currentCoords[1]))
                return True
        elif direction == "down":
            if self.currentCoords[0] + 2 > len(self.map):
                return False
            else:
                self.__internalMove((self.currentCoords[0] + 1, self.currentCoords[1]))
                return True
        else:
            return False
    # Returns the current cell object
    def getInfo(self):
        return self.__getCurrentCell()

class Location():
    def __init__(self, name, uid, category, icon) -> None:
        # Location informations
        self.name = name
        self.uid = uid
        self.category = category
        self.icon = icon

        # Flag that stores if the this is the current location of the player.
        self.playerIsOn = False

    # Returns the icon that should be displayed on the map screen
    def getIcon(self) -> str:
        if self.playerIsOn:
            return MAP_PLAYER_ICON
        else:
            return self.icon
