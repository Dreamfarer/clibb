import sys
import os
from .elements.Navigation import Navigation
from .elements.Action import Action
from .elements.Interactable import Interactable
import shutil


class Window:
    previous_message = None
    previous_line_written = None

    def __init__(self, configuration):
        self.__name = configuration.get("name")
        self.__elements = configuration.get("elements", [])
        self.__color_configuration = configuration.get("colors")
        self.width = configuration.get("width", shutil.get_terminal_size().columns)

        self.__interactable_elements = [
            element for element in self.__elements if isinstance(element, Interactable)
        ]
        if self.__interactable_elements:
            self.__interactable_elements[0].highlight(0)

        if not all([self.__name, self.__elements, self.__color_configuration]):
            raise ValueError(
                "Please provide at least 'name', 'elements' and 'colors' for each window."
            )

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_elements(self):
        return self.__elements

    def run(self):
        # Display every element of the active window
        message = "\n".join(
            [
                element.display(self.__color_configuration, self.width)
                for element in self.__elements
            ]
        )

        # If nothing has changed since the last user interaction, do not redraw window
        if Window.previous_message != message:
            self.__clear_console()
            print(message)
            Window.previous_message = message
            Window.previous_line_written = len(self.__elements)

        # Catch key press by user
        user_input = self.__getch()
        result = {"char": user_input, "name": None}

        # Perform specific actions only when specific user inputs and elements match
        for element in self.__elements:
            if isinstance(element, Action) and element.get_abbreviation() == user_input:
                if not element.get_stealth():
                    self.__clear_console()
                element.execute()
                Window.previous_message = None
            elif (
                isinstance(element, Navigation)
                and element.get_abbreviation() == user_input
            ):
                result["name"] = element.get_name()

        Interactable.navigate(user_input, self.__interactable_elements)
        return result

    def __getch(self):
        if os.name == "nt":
            import msvcrt

            return msvcrt.getch().decode()
        else:
            import termios
            import tty

            old_settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin)
            char = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            return char

    def __clear_console(self):
        # Properly clear the terminal on launch only
        if Window.previous_line_written is None:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            for _ in range(Window.previous_line_written + 1):
                print(end="\033[2K\r\33[A")
