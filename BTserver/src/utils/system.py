import os

class System:

    @staticmethod
    def clear():
        if os.name == "posix":
            os.system("clear")

        elif os.name == "nt":
            os.system("cls")