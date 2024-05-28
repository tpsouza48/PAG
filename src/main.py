from modules.MapHandler import MapHandler
from time import sleep as delay
import os, keyboard

map = MapHandler(xSize=15, ySize=5, startingIndex=(1, 1))

def showMap():
    while True:
        os.system('cls')
        map.show()

        cellInfo = map.getInfo()
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
                else:
                    direction = None

                if direction != None:
                    delay(0.2)
                    break
            except:
                pass

        if direction == "close":
            break
        else:
            map.move(direction)

while True:
    os.system('cls')
    cellInfo = map.getInfo()
    print(f"-- {cellInfo.name} --")

    print("\n1 - Dummy option")
    print("2 - Open map")
    opt = str(input("\n>> "))

    if opt == '1':
        continue
    elif opt == '2':
        showMap()
    else:
        continue
