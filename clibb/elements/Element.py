from abc import ABC, abstractclassmethod
from ..Color import Color

class Element(ABC):

    def __init__(self) -> None:
        self.__row = None

    def reset_color(self, color: Color) -> str:
        return f"\33[0m\u001b[38;2;{color.r};{color.g};{color.b}m"

    def draw_foreground(self, color: Color) -> str:
        return f"\u001b[38;2;{color.r};{color.g};{color.b}m"

    def draw_background(self, color: Color) -> str:
        return f"\u001b[48;2;{color.r};{color.g};{color.b}m"
    
    def get_row(self) -> int:
        return self.__row
    
    def set_row(self, row: int) -> None:
        self.__row = row

    @abstractclassmethod
    def display(self) -> None:
        pass