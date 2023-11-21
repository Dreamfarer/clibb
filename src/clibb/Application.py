from .Window import Window
from typing import Union
from collections import deque


class Application:
    def __init__(self) -> None:
        self.__windows = []
        self.__history = deque()

    def run(self) -> None:
        """
        Run CLIBB!
        """
        if not len(self.__windows):
            raise Exception("No windows found. Please add windows with instance.add()!")
        if not len(self.__history):
            raise Exception("No window has been actiavated.")
        self.__switch_window(self.__history[-1].run())
        self.run()

    def activate(self, name: Union[Window, dict, str]) -> None:
        """
        Activate the window by referencing it with either its name ('str'),
        its configuration ('dict') or the object itself ('Window').

        Raise 'Exception' if the referenced window does not exist.
        """
        window = self.__find_window(name)
        if len(self.__history) >= 2 and self.__history[-2] == window:
            self.__history.pop()
        else:
            self.__history.append(window)

    def add(self, *windows: Union[Window, dict, tuple, list]) -> None:
        """
        Add windows by referencing them with either its configuration ('dict')
        or the object itself ('Window').
        The reference can be passed as standalone parameters or within tuples and lists.

        Raise 'Exception' if the referenced window does not exist.
        """
        for window in windows:
            if isinstance(window, (Window, dict)):
                self.__windows.append(
                    Window(window) if isinstance(window, dict) else window
                )
            elif isinstance(window, (tuple, list)):
                self.add(*window)
            else:
                raise TypeError(
                    "Elements of 'windows' must be of type 'dict' (configuration) or 'Window' (object) as a standalone variable or wrapped inside a tuple or list."
                )
            elements = self.__windows[-1].get_elements()
            for row, element in enumerate(elements):
                element.set_row(row)

    def remove(self, *windows: Union[Window, dict, tuple, list, str]) -> None:
        """
        Remove windows by referencing them with either its name ('str'),
        its configuration ('dict') or the object itself ('Window').
        The reference can be passed as standalone parameters or within tuples and lists.

        Raise 'Exception' if the referenced window does not exist.
        """
        for window in windows:
            if isinstance(window, (Window, dict, str)):
                reference = self.__find_window(window)
                if self.__history and self.__history[-1] == reference:
                    self.__switch_window({"char": "e"})
                self.__windows.remove(reference)

            elif isinstance(window, (list, tuple)):
                self.remove(*window)

            else:
                raise TypeError(
                    "Elements of 'windows' must be of type 'dict' (configuration) or 'Window' (object) as a standalone variable or wrapped inside a tuple or list. Alternatively, the window can be delted by supplying its name in type 'str'."
                )

    def __find_window(self, identifier: Union[str, dict, Window]) -> Window:
        """
        Find the window matching the identifier. The identifier can either be its
        name ('str'), its configuration ('dict') or the object itself ('Window').

        Raise 'Exception' if the referenced window does not exist.
        """
        for window in self.__windows:
            if isinstance(identifier, str):
                if str(window) == identifier:
                    return window
            if isinstance(identifier, dict):
                try:
                    if str(window) == identifier["name"]:
                        return window
                except:
                    raise Exception(f"Window configuration is lacking 'name' key")
            elif isinstance(identifier, Window):
                if window == identifier:
                    return window
        raise Exception(f"Window does not exist")

    def __switch_window(self, user_choice: dict):
        """
        Switch to the window denoted by the 'name' key of 'user_choice'.
        Return to the previous window if the 'char' key is equal to 'e'.
        """
        try:
            self.activate(user_choice["name"])
        except:
            if user_choice["char"] == "e":
                self.__history.pop()
                if not self.__history:
                    quit()
