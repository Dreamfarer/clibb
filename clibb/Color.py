class Color():

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def get_tuple(self) -> list:
        return (self.r, self.g, self.b)
    
    def get_dict(self) -> dict:
        return {"r": self.r, "g": self.g, "b": self.b}