from PIL import Image
import random
import pygame
import os
from Functionality.data import path

def PickImage(size):
    images = os.listdir(path("Resources\Images\Game Images"))
    image_path = path(f"Resources/Images/Game Images/{random.choice(images)}") # Selecting random image
    colors = Image.open(image_path).convert("RGB").getcolors(100000)
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, size)

    colors = [list(i) for i in colors]
    for i in colors: i.remove(i[0])
    colors = [i[0] for i in colors]

    color = random.choice(colors)
    return [image, color]