from typing import Union, Callable


class Mutable:
    """
    A container that holds a value of type 'str', 'int', 'float', 'bool'
    or a function that evaluates to a 'str'-convertible value.
    The container allows these usually non-mutable types to be mutable by reference.
    """

    def __new__(cls, value: Union[float, int, str, bool, Callable]) -> "Mutable":
        if isinstance(value, (float, int, str, bool, Callable)):
            return object.__new__(cls)
        if isinstance(value, Mutable):
            return value
        raise TypeError(
            "'Mutable' must be instanciated with a parameter of type 'str', 'int', 'float', 'bool' or 'callable'."
        )

    def __init__(self, value: Union[float, int, str, bool, Callable]) -> None:
        self.set(value)

    def __str__(self) -> str:
        """
        Return a string representation of the contained value.
        If the value is a callable, it evaluates and returns its string representation.
        """
        if isinstance(self.__value, Callable):
            try:
                result = str(self.__value())
            except Exception as e:
                raise ValueError(
                    "Callable must return a string-convertible value."
                ) from e
            return result
        return str(self.__value)

    def __len__(self) -> int:
        return len(str(self))

    def unwrap(self) -> Union[float, int, str, bool, Callable]:
        """
        Unwrap the variable that is wrapped inside the 'Mutable' container.
        """
        return self.__value

    def set(self, value: Union[float, int, str, bool, Callable]) -> "Mutable":
        """
        Assign a new value to this object and return the object.
        """
        self.__check(value, float, int, str, bool, Callable, Mutable)
        self.__value = str(value) if not callable(value) else value
        return self

    def __check(self, value: Union[float, int, str, Callable], *types) -> None:
        """
        Check if 'value' is of a given type or types. Raise TypeError if not.
        """
        if not isinstance(value, types):
            expected_types = ", ".join(t.__name__ for t in types)
            raise TypeError(
                f"Expected type(s): {expected_types}, got: {type(value).__name__}"
            )
