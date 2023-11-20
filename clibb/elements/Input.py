from typing import Union
from ..Mutable import Mutable
from .Element import Element
from .Interactable import Interactable


class Input(Element, Interactable):
    def __init__(
        self,
        name: Union[Mutable, str],
        variable: Union[Mutable, str],
    ) -> None:
        self.__variable = Mutable(variable)
        self.__message = {"name": Mutable(name).set(f" {name}")}
        self.__width = None
        Interactable.__init__(self)
        Element.__init__(self)

    def select(self, index: int) -> None:
        moves_up = self.get_row() + 1
        moves_forward = (
            len(str(self.__message["name"]))
            + 3
            + len(self.__calculate_whitespaces(self.__message, self.__width))
        )
        print(f"\x1b[{moves_up};{moves_forward}H\x1b[0K", end="")
        user_input = input()
        self.__variable.set(Mutable(f"{user_input}"))

    def __len__(self) -> list:
        return 1

    def display(self, color_configuration: dict, width: int) -> str:
        self.__width = width
        message = f"{self.__message['name']}{self.__calculate_whitespaces(self.__message, width)}"
        message += f"> {self.draw_background(color_configuration['pass']) if self.highlighted() != None else ''}"
        return (
            message
            + f"{self.__variable}{self.reset_color(color_configuration['text'])} "
        )

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        return " " * ((width // 3 - 4) - len(message["name"]))
