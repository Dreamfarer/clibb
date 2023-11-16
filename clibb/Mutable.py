from typing import Union, Callable


class Mutable:
    """
    A container that holds a value of type 'str', 'int', 'float', or a function
    that evaluates to a 'str'-convertible value. The container allows
    these usually non-mutable types to be mutable by reference.
    """

    def __new__(cls, message: Union[float, int, str, Callable]) -> "Mutable":
        if isinstance(message, (float, int, str, Callable)):
            return object.__new__(cls)
        if isinstance(message, Mutable):
            return message
        raise TypeError(
            "'Mutable' must be instanciated with a parameter of type 'str', 'int', 'float' or 'callable'."
        )

    def __init__(self, message: Union[float, int, str]) -> None:
        self.set(message)

    def __str__(self) -> str:
        """
        Return a string representation of the contained value.
        If the value is a callable, it evaluates and returns its string representation.
        """
        if isinstance(self.__message, Callable):
            try:
                result = str(self.__message())
            except Exception as e:
                raise ValueError(
                    "Callable must return a string-convertible value."
                ) from e
            return result
        return str(self.__message)

    def __len__(self) -> int:
        return len(str(self))

    def set(self, message: Union[float, int, str, Callable]) -> "Mutable":
        """
        Assign a new value to this object and return the object.
        """
        self.__check(message, float, int, str, Callable, Mutable)
        self.__message = str(message) if not callable(message) else message
        return self

    def __check(self, message: Union[float, int, str, Callable], *types) -> None:
        """
        Check if 'message' is of a given type or types. Raise TypeError if not.
        """
        if not isinstance(message, types):
            expected_types = ", ".join(t.__name__ for t in types)
            raise TypeError(
                f"Expected type(s): {expected_types}, got: {type(message).__name__}"
            )
