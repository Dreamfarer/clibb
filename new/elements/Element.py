from abc import ABC, abstractclassmethod
from Color import Color

class Element(ABC):

    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def display(self):
        pass

    def reset_color(self, color):
        return f"\33[0m\u001b[38;2;{color.r};{color.g};{color.b}m"

    def draw_foreground(self, color):
        return f"\u001b[38;2;{color.r};{color.g};{color.b}m"

    def draw_background(self, color):
        return f"\u001b[48;2;{color.r};{color.g};{color.b}m"