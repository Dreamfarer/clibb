from typing import Union, Callable
from ..Mutable import Mutable
from .Element import Element


class Display(Element):

    """
    Element that displays text on the left side, followed by a variable value
    on the right side.
    """

    def __init__(
        self, message: Union[Mutable, str], variable: [Mutable, str, Callable]
    ) -> None:
        self.__message = {
            "message_left": Mutable(message),
            "message_right": Mutable(variable),
        }
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        message = str(self.__message["message_left"])
        message += self.__calculate_whitespaces(self.__message, width)
        message += str(self.__message["message_right"])
        message += self.reset_color(color_configuration["text"])
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        return " " * ((width // 3 - 2) - len(message["message_left"]))
