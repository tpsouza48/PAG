class Player():
    def __init__(self, name, hp=100) -> None:
        self.name = name
        self.hp = hp

        self.inventory = []