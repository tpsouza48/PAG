from modules.MapHandler import MapHandler
import os

map = MapHandler(xSize=15, ySize=5, startingIndex=(1, 1))

def showMap():
    while True:
        os.system('cls')
        map.show()

        cellInfo = map.getInfo()
        print(f"\nYou are in: {cellInfo.name}")

        direction = input(">> ")

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
