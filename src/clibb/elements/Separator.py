from .Element import Element


class Separator(Element):
    """
    Element that represents an empty or a filled separator line.
    """

    def __init__(self, state: str) -> None:
        if not state in ["filled", "empty"]:
            TypeError(f"Expected <class 'str'>: 'filled' or 'empty'")
        self.__state = state
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        """
        Constructs and returns a string representation of the seperator element.
        """
        if self.__state == "filled":
            message = self.draw_foreground(color_configuration["background"])
            message += "▁" * width
            message += self.reset_color(color_configuration["text"])
            return message
        else:
            return ""
