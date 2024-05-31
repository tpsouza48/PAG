from modules.MapHandler import MapHandler
from modules.SoundHandler import SoundHandler
from modules.Player import Player
from modules.InputManager import InputManager
from rich.console import Console
from time import sleep as delay
from random import randint
import os, keyboard

class Game():
    def __init__(self) -> None:
        self.running = False

        self.con = Console()
        self.sound = SoundHandler()
        self.map = MapHandler(self.con, xSize=15, ySize=5, startingIndex=(randint(0, 4), randint(0, 14)))
        self.inputManager = InputManager(self.con)
        self.player = None

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def showMap(self):
        while True:
            self.clear()
            self.map.show()

            cellInfo = self.map.getInfo()
            self.con.print(f"\nYou are in: [bold]{cellInfo.name}[/].\nPress [bold]ENTER[/] to exit the map.")

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
            self.con.print(f"-- {cellInfo.name} --")

            self.con.print("\n1 - What's my name?")
            self.con.print("2 - Open map")
            opt = str(self.con.input("\n>> "))

            if opt == '1':
                self.sound.play("C:/Users/pcrub/Documents/GitHub/PAG/src/modules/theme.mp3")
                self.con.print(self.player.name)
                self.con.input()
            elif opt == '2':
                self.showMap()
            else:
                continue
    
    def createPlayer(self):
        name = self.inputManager.strInput("[blue]What is your name?[/] >> ", errMsg=None)
        confirm = self.inputManager.yesNo(f"\nYour character will be called [underline]{name}[/].\nDo you confirm? (y/n) >> ")

        if not confirm:
            self.clear()
            return self.createPlayer()

        self.player = Player(name, 100, {})

    def run(self):
        self.clear()
        self.createPlayer()

        self.running = True
        self.__mainLoop()

game = Game()
game.run()