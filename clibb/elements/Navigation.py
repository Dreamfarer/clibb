from typing import Union
from ..Mutable import Mutable
from .Element import Element

class Navigation(Element):

    def __init__(self, abbreviation: Union[Mutable, str], name: Union[Mutable, str], variable: Union[Mutable, str] = None) -> None:
        if variable == None: 
            self.__message = {
                "abbreviation": Mutable.new(abbreviation).set(f" {abbreviation} "), 
                "name": Mutable.new(name).set(f" {name}")
                }
        else:
            self.__message = {
                "abbreviation": Mutable.new(abbreviation).set(f" {abbreviation} "), 
                "name": Mutable.new(name).set(f" {name}"),
                "variable": Mutable.new(variable)
                }
        super().__init__()

    def get_name(self) -> str:
        return str(self.__message["name"]).strip()

    def get_abbreviation(self) -> str:
        return str(self.__message["abbreviation"]).strip()

    def display(self, color_configuration: dict, width: int) -> None:
        message = self.draw_background(color_configuration["background"])
        message += str(self.__message["abbreviation"])
        message += self.reset_color(color_configuration["text"]) 
        message += str(self.__message["name"])
        if "variable" in self.__message:
            message += self.__calculate_whitespaces(self.__message, width)
            message += str(self.__message["variable"])
        message += self.reset_color(color_configuration["text"])
        return message

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        return " " * ((width // 3 - 2) - len(message["abbreviation"]) - len(message["name"]))