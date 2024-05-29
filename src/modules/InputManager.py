class InputManager():
    def __init__(self, icon=">> ") -> None:
        self.icon = icon

    # Used all across functions to accept and validate string-only input
    def strInput(self, text, errMsg="You should type text. Try again!") -> str:
        """
        Validates and returns a string of input.

        Args:
            text (str):     The text that appears on the input function.
            errMsg (str):   This argument allows the customization of the error message.

        Returns:
            str:    The already validated input the user entered.
        """
        inp = str(input(text))

        if inp == "":
            # If no error message, we jump the print and "enter to continue"
            if errMsg: 
                print(errMsg)
                input()
            
            return self.strInput(text, errMsg=errMsg)
        else:
            return inp
        
    def yesNo(self, text, errMsg="Invalid option. Try again."):
        opt = str(input(text)).lower()

        if opt in ("yes", "y"):
            return True
        elif opt in ("no", "n"):
            return False
        else:
            # If no error message, we jump the print and "enter to continue"
            if errMsg: 
                print(errMsg)
                input()
            
            return self.yesNo(text, errMsg=errMsg)