import pygame
import math

pygame.init()

class Shape:
    def __init__(self):
        self.unit = "meters"

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        return (f"Circle - Radius: {self.radius} {self.unit}\n"
                f"Area: {self.area()} {self.unit} squared\n"
                f"Perimeter: {self.perimeter()} {self.unit}")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        return (f"Rectangle - Width: {self.width} {self.unit}, Height: {self.height} {self.unit}\n"
                f"Area: {self.area()} {self.unit} squared\n"
                f"Perimeter: {self.perimeter()} {self.unit}")

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming it's an equilateral triangle, otherwise, you'd need more information
        return 3 * self.base

    def display(self):
        return (f"Triangle - Base: {self.base} {self.unit}, Height: {self.height} {self.unit}\n"
                f"Area: {self.area()} {self.unit} squared\n"
                f"Perimeter: {self.perimeter()} {self.unit}")

# Initialize Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes in Pygame")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

def display_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Sample calls
circle = Circle(50)
rectangle = Rectangle(100, 60)
triangle = Triangle(60, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    display_text(circle.display(), 50, 50, RED)
    pygame.draw.circle(screen, RED, (200, 200), circle.radius)

    display_text(rectangle.display(), 50, 300, RED)
    pygame.draw.rect(screen, RED, (200, 300, rectangle.width, rectangle.height))

    display_text(triangle.display(), 50, 500, RED)
    pygame.draw.polygon(screen, RED, [(200, 500), (200 + triangle.base, 500), (200 + triangle.base / 2, 500 - triangle.height)])

    pygame.display.flip()

pygame.quit()
