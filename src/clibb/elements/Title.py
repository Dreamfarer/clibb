from typing import Union, Callable
from ..Mutable import Mutable
from .Element import Element


class Title(Element):
    """
    Element that shows left- and right-aligned text, the state of a variable, or the output of a function in inverted colors.
    """

    def __init__(
        self,
        message_left: Union[Mutable, str, Callable],
        message_right: Union[Mutable, str, Callable] = None,
    ) -> None:
        if message_right == None:
            self.__message = {"message_left": Mutable(message_left)}
        else:
            self.__message = {
                "message_left": Mutable(message_left),
                "message_right": Mutable(message_right),
            }
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        """
        Constructs and returns a string representation of the title element.
        """
        message = self.draw_background(color_configuration["background"])
        message += str(self.__message["message_left"])
        message += self.__calculate_whitespaces(self.__message, width)
        if "message_right" in self.__message:
            message += str(self.__message["message_right"])
        message += self.reset_color(color_configuration["text"])
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        """
        Calculates and returns the whitespace needed for alignment in the console.
        """
        if not "message_right" in self.__message:
            return " " * (width - len(message["message_left"]))
        return " " * (
            width - len(message["message_right"]) - len(message["message_left"])
        )
