from modules.MapHandler import MapHandler
from modules.SoundHandler import SoundHandler
from modules.Player import Player
from modules.InputManager import InputManager
from modules.GlobalConf import DEBUG
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
        delay(0.1)
        self.con.rule("World Map")
        while True:
            self.clear()
            self.map.show()

            cellInfo = self.map.getInfo()
            self.con.print(f"\nYou are in: [bold]{cellInfo.name}[/].\nPress [bold]ENTER[/] to exit the map.")

            direction = None

            keyboard.block_key("enter")
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
                        delay(0.1)
                        break
                except:
                    pass
            
            if direction == "close":
                keyboard.unblock_key("enter")
                break
            
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
    
    def __pickName(self):
        # Choosing name
        self.con.rule("Choose your name")
        name = self.inputManager.strInput("[blue]What is your name?[/] >> ", errMsg=None)
        confirm = self.inputManager.yesNo(f"\nYour character will be called [underline]{name}[/].\nDo you confirm? (y/n) >> ")

        if not confirm:
            self.clear()
            return self.__pickName()

    def __pickAttrs(self):
        self.clear()
        self.con.rule("Pick your attributes")

        attr = {
            "charisma": 5,
            "intelligence": 5,
            "luck": 5,
        }
        pointsLeft = 4
        
        buffer = {0: "Please pick your stats below using the arrow keys.",
                  1: "Press ENTER to pick the next stat.",
                  "points": f"Points remaining: [bold green]{pointsLeft}[/]",
                  "": ""}
        updated = True

        # Blocks the enter key from submiting the confirm at the end.
        keyboard.block_key("enter")
        # For each attribute, we do the same.
        for key, value in attr.items():
            buffer.update({key: f"{key}  |  << {attr[key]} >>"})
            while True:
                if updated:
                    self.clear()
                    self.con.rule("Pick your attributes")
                    for i, value in buffer.items():
                        self.con.print(value.capitalize())
                    updated = False
                
                delay(0.1)
                if keyboard.is_pressed("left"):
                    if attr[key] > 0: 
                        attr[key] -= 1
                        pointsLeft += 1
                        buffer.update({key: f"{key}  |  << {attr[key]} >>"})
                        buffer["points"] = f"Points remaining: [bold green]{pointsLeft}[/]"
                        updated = True
                        delay(0.1)
                elif keyboard.is_pressed("right"):
                    if pointsLeft > 0 and attr[key] < 10:
                        attr[key] += 1
                        pointsLeft -= 1
                        buffer.update({key: f"{key}  |  << {attr[key]} >>"})
                        buffer["points"] = f"Points remaining: [bold green]{pointsLeft}[/]"
                        updated = True
                        delay(0.1)
                elif keyboard.is_pressed("enter"):
                    updated = True
                    delay(0.1)
                    break
        # Unblocking now so the user can confirm their choice.
        keyboard.unblock_key("enter")

        confirm = self.inputManager.yesNo("\nThese will be your attributes.\nDo you confirm? >> ")
        if not confirm:
            return self.__pickAttrs()

    def createPlayer(self):
        if DEBUG:
            attrs = self.__pickAttrs()
            self.player = Player("Thiago", 100, attrs)
        else:
            name = self.__pickName()
            attrs = self.__pickAttrs()
            self.player = Player(name, 100, attrs)

    def run(self):
        self.clear()
        self.createPlayer()

        self.running = True
        self.__mainLoop()

game = Game()
game.run()