from elements.Element import Element

class Display(Element):

    def __init__(self, message: str, variable: str) -> None:
        self.__message = {"message_left": " " + message, "message_right": variable}
        super().__init__()

    def __calculate_whitespaces(self, message: dict, width: int) -> str:
        return " " * ((width // 2 - 2) - len(message["message_left"]))

    def display(self, color_configuration: dict, width: int) -> None:
        message = self.__message["message_left"]
        message += self.__calculate_whitespaces(self.__message, width)
        message += self.__message["message_right"]
        message += self.reset_color(color_configuration["text"])
        print(message)