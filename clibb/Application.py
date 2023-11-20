from .Window import Window
from typing import Union


class Application:
    def __init__(self) -> None:
        self.__windows = []
        self.__window_history = []

    def run(self) -> None:
        """
        Run CLIBB! Remember to add windows first with instance.add() before
        calling CLIBB.
        """
        if not len(self.__windows):
            raise Exception("No windows found. Please add windows with instance.add()!")

        # Returns the option the user has selected in the active window
        user_choice = self.__windows[self.__window_history[-1]].run()

        # Return from current window
        if user_choice["char"] == "e":
            if len(self.__window_history) >= 2:
                self.__window_history = self.__window_history[:-1]
            else:
                return

        # Change windows
        else:
            index = self.__find_window_index(user_choice["name"])
            if index != -1:
                self.__add_to_history(index)

        self.run()

    def add(self, *windows) -> None:
        """
        Add windows by 'dict' (configuration) or 'Window' (object)
        to the application. These can be passed as standalone parameters
        or within tuples and lists.
        """
        for window in windows:
            if isinstance(window, Window):
                self.__windows.append(window)
            elif isinstance(window, dict):
                self.__windows.append(Window(window))
            elif isinstance(window, tuple) or isinstance(window, list):
                self.add(*window)
            else:
                raise TypeError(
                    "Elements of 'windows' must be of <class 'dict'> and/or <class 'Window'>"
                )
            elements = self.__windows[-1].get_elements()
            for row, element in enumerate(elements):
                element.set_row(row)
        if not len(self.__window_history):
            self.__add_to_history(0)

    def remove(self, *windows) -> None:
        """
        Remove windows by referencing them with 'str' (name),
        'dict' (configuration) or 'Window' (object). The reference can be
        passed as standalone parameters or within tuples and lists.

        Raise 'Exception' if the referenced window does not exist.
        """
        for name in windows:
            if isinstance(name, (str, dict, Window)):
                index = self.__find_window_index(name)
                if index == -1:
                    raise Exception(f"Window does not exist")
                del self.__windows[index]
                if (
                    self.__window_history[-1] == index
                    or self.__window_history[-1] > len(self.__windows) - 1
                ):
                    self.__window_history[-1] = len(self.__windows) - 1
            elif isinstance(name, (list, tuple)):
                self.remove(*name)
            else:
                raise TypeError("Elements of 'windows' must be of <class 'str'>")

    def activate(self, name: Union[str, dict, Window]) -> None:
        """
        Activate the window by referencing it with 'str' (name),
        'dict' (configuration) or 'Window' (object).

        Raise 'Exception' if the referenced window does not exist.
        """
        index = self.__find_window_index(name)
        if index == -1:
            raise Exception(f"Window does not exist")
        self.__window_history[-1] = index

    def __find_window_index(self, window_or_name: Union[str, dict, Window]) -> int:
        for index, window in enumerate(self.__windows):
            if isinstance(window_or_name, str):
                if str(window) == window_or_name:
                    return index
            elif isinstance(window_or_name, dict):
                try:
                    if str(window) == window_or_name["name"]:
                        return index
                except:
                    raise Exception(f"Window configuration is lacking 'name' key")
            elif isinstance(window_or_name, Window):
                if window == window_or_name:
                    return index
        return -1

    def __add_to_history(self, new_index: int) -> None:
        if new_index in self.__window_history:
            list_index = self.__window_history.index(new_index)
            self.__window_history = self.__window_history[: list_index + 1]
        else:
            self.__window_history.append(new_index)
