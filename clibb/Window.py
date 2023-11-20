import sys
import os
from .elements.Navigation import Navigation
from .elements.Action import Action
from .elements.Interactable import Interactable
import shutil


class Window:
    """
    The Window class represents a single window within the CLIBB framework. It manages
    the display and interaction of various elements within the command line interface.
    """

    previous_message = None
    previous_line_written = None

    def __init__(self, configuration: dict):
        self.__name = configuration.get("name")
        self.__elements = configuration.get("elements", [])
        self.__color_configuration = configuration.get("colors")
        self.width = configuration.get("width")
        self.__flexible_width = self.width is None
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

    def get_elements(self) -> list:
        """
        Retrieves all elements assigned to the window.
        """
        return self.__elements

    def run(self) -> dict:
        """
        Renders the CLI window and handles user input. It updates the window display
        on each element change and determines actions to execute based on user input.

        This method is not intended to be called directly by the user.
        It should be used via the 'clibb.Application' class.
        """
        self.__refresh(self.__build_window(self.__get_width()))
        return self.__act(self.__get_character())

    def __act(self, user_input: str) -> dict:
        """
        Processes user input and determines corresponding actions.
        """
        result = {"char": user_input, "name": None}
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

    def __refresh(self, message: str) -> None:
        """
        Updates the console display if the window's content has changed.
        """
        if Window.previous_message != message:
            self.__clear_console()
            print(message)
            Window.previous_message = message
            Window.previous_line_written = len(self.__elements)

    def __build_window(self, width: int) -> str:
        """
        Constructs the string representation of the window.
        """
        return "\n".join(
            [
                element.display(self.__color_configuration, width)
                for element in self.__elements
            ]
        )

    def __get_width(self) -> int:
        """
        Determines the width of the window based on the console's size.
        """
        if self.__flexible_width:
            self.width = shutil.get_terminal_size().columns
        return self.width

    def __get_character(self) -> str:
        """
        Captures a single keystroke from the user in a cross-platform manner.
        """
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

    def __clear_console(self) -> None:
        """
        Clears the console to update the display without causing flickering.
        """
        if Window.previous_line_written is None:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            for _ in range(Window.previous_line_written + 1):
                print(end="\033[2K\r\33[A")
