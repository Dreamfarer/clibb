from .Window import Window
from typing import Union

class Application():

    def __init__(self) -> None:
        self.__windows = []

    def __find_index_by_name(self, name: str) -> int:
        for index, window in enumerate(self.__windows):
            if window.get_name() == name:
                return index
        return -1
        
    def run(self) -> None:

        # Returns the option the user has selected in the active window
        user_choice = self.__activeWindow.run()

        # Return from current window
        if user_choice["char"] == "e":
            if self.__activeWindow.get_name() != "Home":
                self.__activeWindow = self.__windows[self.__find_index_by_name("Home")]
            else: return
        
        # Change window
        else:
            index = self.__find_index_by_name(user_choice["name"])
            if index != -1: self.__activeWindow = self.__windows[index]

        self.run()

    def add_window(self, configuration: Union[dict, Window]) -> None:

        if isinstance(configuration, Window): self.__windows.append(configuration)
        elif isinstance(configuration, dict): self.__windows.append(Window(configuration))
        else: raise TypeError("'configuration' must be a 'dict' or a 'Window'")

        self.__activeWindow = self.__windows[-1]

    def remove_window(self, name: str) -> None:
        # ...
        pass