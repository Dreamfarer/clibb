from typing import Union

class Mutable():
    """
    A container that holds a variable of type 'str', 'int' or 'float'.
    The usually non-mutable types will become mutable because the container 
    object is passed by reference and not by value.

    If the 'message' parameter is of the same type ('Mutable'), 
    it will simply return the parameter without modification.

    If the 'message' parameter is of another type not mentioned before, 
    it will raise a 'TypeError'.
    """

    def __new__(cls, message:  Union[float, int, str]) -> "Mutable":
        if isinstance(message, (float, int, str)): return object.__new__(cls)
        if isinstance(message, Mutable): return message
        raise TypeError("'Mutable' must be instanciated with a parameter of type 'str', 'int' or 'float'")

    def __init__(self, message: Union[float, int, str]) -> None:
        self.set(message)
        
    def __str__(self) -> str: return str(self.__message)
    def __repr__(self) -> str: return str(self.__message)
    def __len__(self) -> int: return len(str(self))

    def set(self, message: Union[float, int, str]) -> "Mutable":
        """
        Assign 'message' to this object and return the object.
        """
        self.__check(message, float, int, str, Mutable)
        self.__message = str(message)
        return self

    def __check(self, message: Union[float, int, str], *types) -> None:
        """
        Throw error if 'message' is not a type of 'types'.
        """
        for required_type in types:
            if isinstance(message, required_type): return
        raise TypeError(f"Expected {', '.join(required_type)}")