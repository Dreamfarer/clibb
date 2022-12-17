import sys
from elements.Menu import Menu

class Window():

    def __init__(self, configuration: dict) -> None:
        try:
            self.__name = configuration["name"]
            self.__elements = configuration["elements"]
            self.__color_configuration = configuration["colors"]
            self.__width = configuration["width"]
        except:
            raise Warning("Please provide 'name', 'elements', 'colors' and 'width' for each window.")

    def __repr__(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def getch(self) -> str:
        try:
            import msvcrt
            return msvcrt.getch().decode()
        except ImportError:
            import termios
            import tty

            old_settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin)
            char = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            return char

    def run(self) -> dict:

        # Render all elements that belong to this window
        for element in self.__elements:
            element.display(self.__color_configuration, self.__width)

        user_input = self.getch()

        # Retrieve what the user input leads to (abbreviation to name
        for element in [x for x in self.__elements if type(x) == Menu]:
            if element.get_abbreviation() == user_input:
                return {"char": user_input, "name": element.get_name()}
        return {"char": user_input, "name": None}
    
    