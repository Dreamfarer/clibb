from typing import Union

class Mutable():

    def __init__(self, message: Union[float, int, str]) -> None:
        self.set(message)
        
    def __str__(self) -> str: return str(self.__message)
    def __repr__(self) -> str: return str(self.__message)
    def __len__(self) -> int: return len(str(self))

    def set(self, message: Union[float, int, str]):
        self.__check(message, float, int, str)
        self.__message = message
        return self

    @classmethod
    def new(cls, message):
        if isinstance(message, Mutable): return message
        return Mutable(message)

    def __check(self, message: Union[float, int, str], *types) -> None:
        for required_type in types:
            if isinstance(message, required_type): return
        raise TypeError(f"Expected {', '.join(required_type)}")