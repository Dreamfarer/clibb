import sys
import os
from .elements.Navigation import Navigation
from .elements.Action import Action
from .elements.Interactable import Interactable
import shutil

class Window():
    
    previous_message = None
    previous_line_written = None

    def __init__(self, configuration: dict) -> None:
        try:
            self.__name = configuration["name"]
            self.__elements = configuration["elements"]
            self.__interactable_elements = [element for element in self.__elements if isinstance(element, Interactable)]
            if self.__interactable_elements: self.__interactable_elements[0].highlight(0)
            self.__color_configuration = configuration["colors"]
            if "width" in configuration: self.width = configuration["width"]
        except:
            raise Warning("Please provide at least 'name', 'elements' and 'colors' for each window.")

    def __repr__(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def run(self) -> dict:
        # Calculate console width if it has not been provided by user
        if hasattr(self, "width"): width = self.width
        else: width = shutil.get_terminal_size().columns

        # Display every element of the active window
        message = '\n'.join([element.display(self.__color_configuration, width) for element in self.__elements])

        # If nothing has changed since the last user interaction, do not redraw window
        if not Window.previous_message == message:
            self.__clear_console()
            print(message)
            Window.previous_message = message
            Window.previous_line_written = len(self.__elements)

        # Catch key press by user
        try: user_input = self.__getch()
        except: user_input = None

        result = {"char": user_input, "name": None}

        # Perform specific actions only when specific user inputs and elements match
        for element in self.__elements:
            if isinstance(element, Action) and element.get_abbreviation() == user_input:
                self.__clear_console()
                element.execute()
                Window.previous_message = None
            elif isinstance(element, Navigation) and element.get_abbreviation() == user_input:
                result["name"] = element.get_name()

        Interactable.navigate(user_input, self.__interactable_elements)
        return result

    def __getch(self) -> str:
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

    def __clear_console(self) -> None:
        # Properly clear the terminal on launch only
        if Window.previous_line_written == None:
            if os.name == 'nt': os.system('cls')
            else: os.system('clear')
            return
        for index in range(Window.previous_line_written + 1):
            print(end=f"\033[2K\r\33[A")
            # print(end=f"\033[{index};1H")