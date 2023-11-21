from typing import Union
from ..Mutable import Mutable
from .Element import Element
from .Interactable import Interactable


class Checkbox(Element, Interactable):
    """
    Element that represents a binary state. When activated with 'q',
    it toggles a variable between 'True' and 'False'.
    """

    def __init__(
        self,
        name: Union[Mutable, str],
        variable: Mutable,
    ) -> None:
        self.__message = {"name": Mutable(name)}
        self.__variable = Mutable(variable)
        Interactable.__init__(self)
        Element.__init__(self)

    def __len__(self) -> int:
        """
        Returns the fixed 'length' of the checkbox, which is 1.
        """
        return 1

    def select(self, index: int) -> None:
        """
        Toggles the state of the checkbox. Called when the checkbox is activated.
        """
        self.__variable.set(not self.__variable.unwrap())

    def display(self, color_configuration: dict, width: int) -> str:
        """
        Constructs and returns a string representation of the checkbox element.
        """
        message = f"{self.__message['name']}{self.__calculate_whitespaces(self.__message, width)}"
        message += f"[{self.draw_background(color_configuration['pass']) if self.highlighted() is not None else ''}"
        message += f"{'X' if self.__variable.unwrap() else ' '}"
        message += f"{self.reset_color(color_configuration['text'])}] "
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        """
        Calculates and returns the whitespace needed for alignment in the console.
        """
        return " " * ((width // 3 - 2) - len(message["name"]))
