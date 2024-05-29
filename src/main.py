from modules.MapHandler import MapHandler
from modules.Player import Player
from modules.InputManager import InputManager
from time import sleep as delay
from random import randint
import threading  # -> Use threading to implement sound and music later.
import os, keyboard

class Game():
    def __init__(self) -> None:
        self.running = False

        self.map = MapHandler(xSize=15, ySize=5, startingIndex=(randint(0, 4), randint(0, 14)))
        self.stdin = InputManager()
        self.player = None

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def showMap(self):
        while True:
            os.system('cls')
            self.map.show()

            cellInfo = self.map.getInfo()
            print(f"\nYou are in: {cellInfo.name}.\nPress ENTER to exit the map.")

            direction = None

            delay(0.2)
            while True:
                try:
                    direction = None

                    if keyboard.is_pressed('up'): 
                        direction = "up"
                    elif keyboard.is_pressed('down'): 
                        direction = "down"
                    elif keyboard.is_pressed('left'): 
                        direction = "left"
                    elif keyboard.is_pressed('right'): 
                        direction = "right"
                    elif keyboard.is_pressed('enter'):
                        direction = "close"

                    if direction != None:
                        break
                except:
                    pass

            if direction == "close":
                break
            else:
                self.map.move(direction)

    def __mainLoop(self):
        while self.running:
            self.clear()
            cellInfo = self.map.getInfo()
            print(f"-- {cellInfo.name} --")

            print("\n1 - What's my name?")
            print("2 - Open map")
            opt = str(input("\n>> "))

            if opt == '1':
                print(self.player.name)
                input()
            elif opt == '2':
                self.showMap()
            else:
                continue
    
    def createPlayer(self):
        name = self.stdin.strInput("What is your name? >> ", errMsg=None)
        confirm = self.stdin.yesNo(f"\nYour character will be called {name}.\nDo you confirm? (y/n) >> ")
        
        while not confirm:
            self.clear()
            name = self.stdin.strInput("What is your name? >> ", errMsg=None)
            confirm = self.stdin.yesNo(f"\nYour character will be called {name}.\nDo you confirm? (y/n) >> ")

        self.player = Player(name, 100, {})

    def run(self):
        self.clear()
        self.createPlayer()

        self.running = True
        self.__mainLoop()

game = Game()
game.run()