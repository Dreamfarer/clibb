from typing import Union
from ..Mutable import Mutable
from .Navigation import Navigation


class Action(Navigation):

    """
    Element that, when activated with 'q', executes the function passed to it on initialization.
    It makes sense to use the function of an object in order for you to be able
    to store and further process the function's output.

    Set 'stealth' to False if CLIBB should clear the console for you
    and appear again after your function has finished executing.
    """

    def __init__(
        self,
        abbreviation: Union[Mutable, str],
        name: Union[Mutable, str],
        stealth=True,
        action=None,
    ) -> None:
        if not callable(action):
            raise TypeError("Expected a function")
        self.__action = action
        self.__stealth = stealth
        super().__init__(abbreviation, name, None)

    def get_stealth(self) -> bool:
        """
        Get the current value of 'stealth'.
        """
        return self.__stealth

    def execute(self) -> any:
        """
        Execute the function passed to 'Action'.
        """
        return self.__action()
