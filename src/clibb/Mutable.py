from typing import Callable, Any


class Mutable:
    """
    The 'Mutable' class is a wrapper that allows any (non-mutable) type,
    class and method to be mutable.

    Make sure that any type and class implements __str__ and any method
    returns a 'str'-convertible value, else you will receive a runtime exception.
    """

    def __new__(cls, value: Any = None) -> "Mutable":
        if isinstance(value, Mutable):
            return value
        return super().__new__(cls)

    def __init__(self, value: Any = None) -> None:
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
                    "Wrapped callable must return a string-convertible value."
                ) from e
            return result
        if self.__value is None:
            return " "
        return str(self.unwrap())

    def __eq__(self, other: object) -> bool:
        if str(self) == str(other):
            return True
        return False

    def __len__(self) -> int:
        return len(str(self))

    def type(self) -> type:
        """
        Get the type of the variable that is wrapped inside the 'Mutable' container.
        """
        return type(self.unwrap())

    def unwrap(self) -> Any:
        """
        Unwrap the variable that is wrapped inside the 'Mutable' container.
        """
        return self.__value

    def set(self, value: Any) -> "Mutable":
        """
        Assign a new value to this object and return the object.
        """
        if isinstance(value, Mutable):
            self.__value = value.unwrap()
        else:
            self.__value = value
        return self
