from typing import Union
from ..Mutable import Mutable
from .Element import Element
from .Interactable import Interactable


class Checkbox(Element, Interactable):
    def __init__(
        self,
        name: Union[Mutable, str],
        variable: Mutable,
    ) -> None:
        self.__message = {"name": Mutable(name).set(f" {name}")}
        self.__variable = Mutable(variable)
        self.__options = tuple([Mutable("[X]")])
        Interactable.__init__(self)
        Element.__init__(self)

    def select(self, index: int) -> None:
        self.__variable.set(not self.__variable.unwrap())
        self.__options = tuple([Mutable(self.__variable.unwrap)])

    def get_elements(self) -> list:
        return self.__options

    def display(self, color_configuration: dict, width: int) -> str:
        message = f"{self.__message['name']}{self.__calculate_whitespaces(self.__message, width)}"
        message += f"[{self.draw_background(color_configuration['pass']) if self.highlighted() is not None else ''}"
        message += f"{'X' if self.__variable.unwrap() else ' '}"
        message += f"{self.reset_color(color_configuration['text'])}] "
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        return " " * ((width // 3 - 2) - len(message["name"]))
