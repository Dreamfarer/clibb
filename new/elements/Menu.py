from elements.Element import Element

class Menu(Element):

    def __init__(self, abbreviation: str, name: str, variable: str = None) -> None:
        if variable == None: 
            self.__message = {
                "abbreviation": " " + abbreviation + "  ", 
                "name": " " + name
                }
        else:
            self.__message = {
                "abbreviation": " " + abbreviation + "  ", 
                "name": " " + name, 
                "variable": variable
                }
        super().__init__()

    def get_name(self) -> str:
        return self.__message["name"].strip()

    def get_abbreviation(self) -> str:
        return self.__message["abbreviation"].strip()

    def __calculateSpace(self, message: dict, width: int) -> str:
        return " " * ((width // 2 - 2) - len(message["abbreviation"]) - len(message["name"]))

    def display(self, color_configuration: dict, width: int) -> str:
        space = self.__calculateSpace(self.__message, width)
        message = self.draw_background(color_configuration["background"])
        message += self.__message["abbreviation"] 
        message += self.reset_color(color_configuration["text"]) 
        message += self.__message["name"]
        if "variable" in self.__message:
            message += space + self.__message["variable"]
        print(message)