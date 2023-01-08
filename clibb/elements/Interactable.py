from abc import ABC, abstractclassmethod
from typing import Union

class Interactable(ABC):

    def __init__(self) -> None: self.__highlighted = None

    def highlight(self, index: int): self.__highlighted = index
    def dehighlight(self): self.__highlighted = None
    def highlighted(self)-> Union[int, None]: return self.__highlighted

    @abstractclassmethod
    def select(self) -> None:
        pass

    @abstractclassmethod
    def get_elements(self) -> list:
        pass

    @classmethod
    def navigate(self, character: str, elements: list) -> None:
        if not character in ["w", "a", "s", "d", "q"] or not elements: return
        currently_highlighted = self.find_highlighted_interactable_element(elements)
        if character == "q": return currently_highlighted["element"].select(currently_highlighted["column"])
        currently_highlighted["element"].dehighlight()
        if character == "w": self.up(elements, currently_highlighted)
        elif character == "s": self.down(elements, currently_highlighted)
        elif character == "a": self.left(currently_highlighted)
        elif character == "d": self.right(currently_highlighted)

    @classmethod
    def find_highlighted_interactable_element(self, elements: list) -> dict:
        for row, element in enumerate(elements):
            column = element.highlighted()
            if not element.highlighted() == None:
                return {"element": element, "column": column, "row": row}

    @classmethod
    def up(self, elements: list, currently_highlighted: dict) -> None:
        new_row_index = self.index_clamp(currently_highlighted["row"] - 1, elements)
        new_column_index = self.index_restrict(currently_highlighted["column"], elements[new_row_index].get_elements())
        elements[new_row_index].highlight(new_column_index)
    
    @classmethod
    def down(self, elements: list, currently_highlighted: dict) -> None:
        new_row_index = self.index_clamp(currently_highlighted["row"] + 1, elements)
        new_column_index = self.index_restrict(currently_highlighted["column"], elements[new_row_index].get_elements())
        elements[new_row_index].highlight(new_column_index)

    @classmethod
    def left(self, currently_highlighted: dict) -> None:
        new_column_index = self.index_clamp(currently_highlighted["column"] - 1, currently_highlighted["element"].get_elements())
        currently_highlighted["element"].highlight(new_column_index)

    @classmethod
    def right(self, currently_highlighted: dict) -> None:
        new_column_index = self.index_clamp(currently_highlighted["column"] + 1, currently_highlighted["element"].get_elements())
        currently_highlighted["element"].highlight(new_column_index)

    @classmethod
    def index_clamp(cls, index: int, elements: list) -> int: 
        return index % len(elements)

    @classmethod
    def index_restrict(cls, index: int, elements: list) -> int: 
        if index >= len(elements): return len(elements) - 1
        if index < 0: return 0
        return index