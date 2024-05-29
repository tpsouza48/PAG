class Player():
    def __init__(self, name, hp, attributes) -> None:
        self.name = name
        self.hp = hp

        self.inventory = []

        self.attributes = attributes