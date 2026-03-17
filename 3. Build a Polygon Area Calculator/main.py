import math

class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if max(self.height, self.width) > 50:
            return('Too big for picture.')
        picture = ""
        for h in range(0, self.height):
            for w in range(0, self.width):
                picture += "*"
            picture+= "\n"
        return picture
        
    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

