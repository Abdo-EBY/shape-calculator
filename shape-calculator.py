class Rectangle:
    width: int
    height: int
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height
    def get_amount_inside(self, shape):
        amount = (self.width // shape.width) * (self.height // shape.height)
        return amount
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def __str__(self):
        return f'Square(side={self.width})'
    def set_side(self, side):
        self.width = side
        self.height = side
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
    def get_area(self):
        area = self.width ** 2
        return area
    def get_perimeter(self):
        perimeter = self.width * 4
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 * 2) ** 0.5
        return diagonal
    def get_picture(self):
        if self.width > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.width
