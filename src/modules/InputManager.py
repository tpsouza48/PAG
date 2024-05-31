class InputManager():
    def __init__(self, console, icon=">> ") -> None:
        self.icon = icon
        self.con = console

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
        inp = str(self.con.input(f"[bold]{text}[/]"))

        if inp == "":
            # If no error message, we jump the print and "enter to continue"
            if errMsg: 
                self.con.print(errMsg)
                self.con.input()
            
            return self.strInput(text, errMsg=errMsg)
        else:
            return inp
        
    def yesNo(self, text, errMsg="Invalid option. Try again.", clear=None):
        opt = str(self.con.input(text)).lower()

        if opt in ("yes", "y"):
            return True
        elif opt in ("no", "n"):
            return False
        else:
            # If no error message, we jump the print and "enter to continue"
            if errMsg: 
                self.con.print(f"[bold red]{errMsg}[/]")
                self.con.input()
            
            return False