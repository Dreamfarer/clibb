from typing import Union
from ..Mutable import Mutable
from .Element import Element
from .Interactable import Interactable


class Configuration(Element, Interactable):
    """
    Element that allows selection among multiple options. Represents a value
    based on which option is currently selected.
    """

    def __init__(
        self, variable: Union[Mutable, str], name: Union[Mutable, str], *options
    ) -> None:
        self.__variable = Mutable(variable)
        self.__message = {"name": Mutable(name)}
        temporary_list = []
        for option in options:
            temporary_list.append(Mutable(option))
        self.__options = tuple(temporary_list)
        Interactable.__init__(self)
        Element.__init__(self)

    def select(self, index: int) -> None:
        """
        Selects one of the available options based on the provided index.
        """
        self.__variable.set(self.__options[index])

    def __len__(self) -> int:
        """
        Returns the number of available options.
        """
        return len(self.__options)

    def display(self, color_configuration: dict, width: int) -> None:
        """
        Constructs and returns a string representation of the configuration element.
        """
        message = str(self.__message["name"])
        message += self.__calculate_whitespaces_center(self.__message, width)
        field_width = 12
        for index, option in enumerate(self.__options):
            if self.highlighted() == index:
                message += self.draw_background(color_configuration["pass"])
            elif str(option) == str(self.__variable):
                message += self.draw_background(color_configuration["background"])
            message += self.__center(str(option), field_width)
            message += self.reset_color(color_configuration["text"])
            message += " "
        return message

    def __calculate_whitespaces_center(self, message: dict, width: int) -> str:
        """
        Calculates and returns the whitespace needed for center alignment in the console.
        """
        return " " * ((width // 3 - 4) - len(message["name"]))

    def __center(self, word: str, desired_length):
        """
        Centers a word within a given length by padding it with spaces.
        """
        filling_character = " "
        required_space = desired_length - len(word)
        space_front = filling_character * (required_space // 2)
        space_back = filling_character * (required_space - (required_space // 2))
        return space_front + word + space_back
