from typing import Union
from ..Mutable import Mutable
from .Element import Element

class Title(Element):

    def __init__(self, message_left: Union[Mutable, str], message_right: Union[Mutable, str] = None) -> None:
        if message_right == None:
            self.__message = {
                "message_left": Mutable(message_left).set(f" {message_left} ")
            }
        else:
            self.__message = {
                "message_left": Mutable(message_left).set(f" {message_left}"),
                "message_right": Mutable(message_right).set(f"{message_right} ")
            }
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        message = self.draw_background(color_configuration["background"])
        message += str(self.__message["message_left"])
        message += self.__calculate_whitespaces(self.__message, width)
        if "message_right" in self.__message:
            message += str(self.__message["message_right"])
        message += self.reset_color(color_configuration["text"])
        return message
        
    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        if not "message_right" in self.__message:
            return " " * (width - len(message["message_left"]))
        return " " * (width - len(message["message_right"]) - len(message["message_left"]))