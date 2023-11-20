from abc import ABC, abstractclassmethod
from typing import Union


class Interactable(ABC):
    def __init__(self) -> None:
        self.__highlighted = None

    def highlight(self, index: int) -> None:
        self.__highlighted = index

    def dehighlight(self) -> None:
        self.__highlighted = None

    def highlighted(self) -> Union[int, None]:
        return self.__highlighted

    @abstractclassmethod
    def select(self) -> None:
        pass

    @abstractclassmethod
    def __len__(self) -> list:
        pass

    @classmethod
    def navigate(cls, character: str, elements: list) -> None:
        if character not in "wasdq" or not elements:
            return
        current = cls.find_highlighted(elements)
        if character == "q":
            return current["element"].select(current["column"])
        current["element"].dehighlight()
        cls.move(character, elements, current)

    @classmethod
    def find_highlighted(cls, elements: list) -> dict:
        for row, element in enumerate(elements):
            column = element.highlighted()
            if column is not None:
                return {"element": element, "column": column, "row": row}

    @classmethod
    def move(cls, direction: str, elements: list, current: dict) -> None:
        row, col = current["row"], current["column"]
        if direction == "w":
            row -= 1
        elif direction == "s":
            row += 1
        elif direction == "a":
            col -= 1
        elif direction == "d":
            col += 1
        new_row = cls.index_clamp(row, len(elements))
        new_col = cls.index_clamp(col, len(current["element"]))
        elements[new_row].highlight(new_col)

    @classmethod
    def index_clamp(cls, index: int, size: int) -> int:
        return max(0, min(index, size - 1))
