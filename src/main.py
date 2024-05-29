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
            os.system('cls')
            cellInfo = self.map.getInfo()
            print(f"-- {cellInfo.name} --")

            print("\n1 - Placeholder")
            print("2 - Open map")
            opt = str(input("\n>> "))

            if opt == '1':
                continue
            elif opt == '2':
                self.showMap()
            else:
                continue
    
    def createPlayer(self):
        nome = self.stdin.strInput("What is your name? >> ", errMsg=None)
        print(nome)
        input()

    def run(self):
        #self.createPlayer()

        self.running = True
        self.__mainLoop()

game = Game()
game.run()