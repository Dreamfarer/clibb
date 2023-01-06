import sys
import os
from .elements.Navigation import Navigation
from .elements.Action import Action
import shutil


class Window():

    previous_message = None

    def __init__(self, configuration: dict) -> None:
        try:
            self.__name = configuration["name"]
            self.__elements = configuration["elements"]
            self.__color_configuration = configuration["colors"]
            if "width" in configuration: self.width = configuration["width"]
        except:
            raise Warning("Please provide 'name', 'elements', 'colors' and 'width' for each window.")

    def __repr__(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return self.__name

    def __clear_console(self) -> None:
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')

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

        if hasattr(self, "width"): width = self.width
        else: width = shutil.get_terminal_size().columns

        message = '\n'.join([element.display(self.__color_configuration, width) for element in self.__elements])

        if not Window.previous_message == message:
            self.__clear_console()
            print(message)
            Window.previous_message = message

        try: user_input = self.getch()
        except: user_input = None

        result = {"char": user_input, "name": None}
        for element in self.__elements:
            if isinstance(element, Action) and element.get_abbreviation() == user_input:
                self.__clear_console()
                element.execute()
                Window.previous_message = None
            elif isinstance(element, Navigation) and element.get_abbreviation() == user_input:
                result["name"] = element.get_name()
        return result