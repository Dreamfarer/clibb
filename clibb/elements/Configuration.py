from typing import Union
from ..Mutable import Mutable
from .Element import Element
from .Interactable import Interactable


class Configuration(Element, Interactable):
    def __init__(
        self, variable: Union[Mutable, str], name: Union[Mutable, str], *options
    ) -> None:
        self.__variable = Mutable(variable)
        self.__message = {"name": Mutable(name).set(f" {name}")}
        temporary_list = []
        for option in options:
            temporary_list.append(Mutable(option))
        self.__options = tuple(temporary_list)
        Interactable.__init__(self)
        Element.__init__(self)

    def select(self, index: int) -> None:
        self.__variable.set(self.__options[index])

    def __len__(self) -> list:
        return len(self.__options)

    def display(self, color_configuration: dict, width: int) -> None:
        message = str(self.__message["name"])
        message += self.__calculate_whitespaces_center(self.__message, width)
        # field_width = (width - len(message) - (len(self.__options))) // len(self.__options)
        field_width = 12  # WIP
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
        return " " * ((width // 3 - 4) - len(message["name"]))

    def __center(self, word: str, desired_length):
        filling_character = " "
        required_space = desired_length - len(word)
        space_front = filling_character * (required_space // 2)
        space_back = filling_character * (required_space - (required_space // 2))
        return space_front + word + space_back
