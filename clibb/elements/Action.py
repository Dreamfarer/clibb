from .Navigation import Navigation

class Action(Navigation):
    def __init__(self, abbreviation: str, name: str, variable: str = None, action = None) -> None:
        super().__init__(abbreviation, name, variable)
        self.__action = action

    def execute(self) -> any:
        return self.__action()