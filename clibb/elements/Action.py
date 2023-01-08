from typing import Union
from ..Mutable import Mutable
from .Navigation import Navigation

class Action(Navigation):
    
    def __init__(self, 
        abbreviation: Union[Mutable, str], name: Union[Mutable, str], 
        variable: Union[Mutable, str] = None, action = None
    ) -> None:

        if not callable(action): raise TypeError("Expected a function")
        self.__action = action
        super().__init__(abbreviation, name, variable)

    def execute(self) -> any:
        return self.__action()