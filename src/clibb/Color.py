class Color:
    """
    The 'Color' class represents one color in the rgb spectrum.
    """

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def get_tuple(self) -> list:
        """
        Get the RGB color as a (red, green, blue) tuple.
        """
        return (self.r, self.g, self.b)

    def get_dict(self) -> dict:
        """
        Get the RGB color as a dictionary with 'r', 'g', and 'b' keys.
        """
        return {"r": self.r, "g": self.g, "b": self.b}
