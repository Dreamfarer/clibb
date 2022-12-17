from elements.Element import Element

class Seperator(Element):
    
    def __init__(self, state: str) -> None:
        self.__state = state
        super().__init__()

    def __calculate_whitespaces(self, width: int) -> str:
        return "_" * width

    def display(self, color_configuration: dict, width: int) -> str:
        if self.__state == "filled":
            message = self.draw_foreground(color_configuration["background"])
            message += self.__calculate_whitespaces(width)
            message += self.reset_color(color_configuration["text"])
            print(message) 
        else: print("")