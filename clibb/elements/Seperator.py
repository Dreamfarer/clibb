from .Element import Element

class Seperator(Element):
    
    def __init__(self, state: str) -> None:
        if not state in ["filled", "empty"]: TypeError(f"Expected <class 'str'>: 'filled' or 'empty'")
        self.__state = state
        super().__init__()

    def display(self, color_configuration: dict, width: int) -> str:
        if self.__state == "filled":
            message = self.draw_foreground(color_configuration["background"])
            message += self.__calculate_whitespaces(width)
            message += self.reset_color(color_configuration["text"])
            return message
        else: return ""

    def __calculate_whitespaces(self, width: int) -> str:
        return "▁" * width