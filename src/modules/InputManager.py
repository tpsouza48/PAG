class InputManager():
    def __init__(self, icon=">> ") -> None:
        self.icon = icon

    # Used all across functions to accept and validate string-only input
    def strInput(self, text) -> str:
        inp = str(input(text))

        if inp == "":
            print("You should type text. Try again!")
            input()
            return self.strInput(text)
        else:
            return inp