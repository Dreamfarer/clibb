from typing import Union, Callable
from ..Mutable import Mutable
from .Element import Element


class Display(Element):

    """
    Element that shows text, the state of a variable, or the output of a function.
    """

    def __init__(
        self, message: Union[Mutable, str, Callable], variable: [Mutable, str, Callable]
    ) -> None:
        self.__message = {
            "message_left": Mutable(message),
            "message_right": Mutable(variable),
        }
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        """
        Constructs and returns a string representation of the display element.
        """
        message = str(self.__message["message_left"])
        message += self.__calculate_whitespaces(self.__message, width)
        message += str(self.__message["message_right"])
        message += self.reset_color(color_configuration["text"])
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        """
        Calculates and returns the whitespace needed for alignment in the console.
        """
        return " " * ((width // 3 - 2) - len(message["message_left"]))
