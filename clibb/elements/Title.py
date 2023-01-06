from .Element import Element

class Title(Element):

    def __init__(self, message_left: str, message_right: str = None) -> None:
        if message_right == None:
            self.__message = {
                "message_left": " " + message_left + " "
            }
        else:
            self.__message = {
                "message_left": " " + message_left,
                "message_right": message_right + " "
            }
        super().__init__()
        
    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        if not "message_right" in self.__message:
            return " " * (width - len(message["message_left"]))
        return " " * (width - len(message["message_right"]) - len(message["message_left"]))

    def display(self, color_configuration: dict, width: int) -> str:
        message = self.draw_background(color_configuration["background"])
        message += self.__message["message_left"]
        message += self.__calculate_whitespaces(self.__message, width)
        if "message_right" in self.__message:
            message += self.__message["message_right"]
        message += self.reset_color(color_configuration["text"])
        return message