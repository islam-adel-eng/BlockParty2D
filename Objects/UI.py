import pygame
from Functionality.data import path

def text(surface, text, size, font_name, color, posX, posY, BG_color = None):
    font = pygame.font.Font(path(f"Resources/Fonts/{font_name}"), size)
    txt = font.render(text, True, color, BG_color)
    text_rect = txt.get_rect()
    text_rect.center = [posX, posY]

    surface.blit(txt, text_rect)

class button():
    def __init__(self, surface, color, size: list, position: list, text, roundness: int,  result: int, state = 0, clicked = False, image: list = None):
        self.surface = surface
        self.color = color
        self.size = size
        self.position = position
        self.text = text
        self.roundness = roundness
        self.result = result
        self.clicked = clicked
        self.state = state
        self.image = image

    def draw(self):
        global Rect

        if self.image == None:
            Rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
            Rect.center = [self.position[0], self.position[1]]

            text(self.surface, self.text, 48, "8-bit Arcade In.ttf", [255,255,255], self.position[0], self.position[1]-5)

        elif self.image != None:
            imageSrc = pygame.image.load(path(f"Resources/UI/{self.image[self.state]}"))
            Rect = imageSrc.get_rect()
            Rect.center = [self.position[0], self.position[1]]

            self.surface.blit(imageSrc, Rect, None)
            text(self.surface, self.text, 48, "8-bit Arcade In.ttf", [255,255,255], self.position[0], self.position[1]-5)

    def hover(self):
        global Rect

        Mpos = pygame.mouse.get_pos()

        if Rect.collidepoint(Mpos):
            self.state = 1
            return True
        else:
            self.state = 0
            return False
        