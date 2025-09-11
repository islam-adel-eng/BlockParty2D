import pygame, sys
from Functionality.data import *
from Objects.UI import *

class stats():
    def __init__(self):
        self.Resolution = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.BGcolor = [255, 228, 159]
        self.screen = pygame.display.set_mode(self.Resolution)

        self.Clock = pygame.time.Clock()
        self.FPS = 60
        self.Running = True
    
    def loop(self):
        pygame.display.set_caption("Stats")
        while self.Running:
            self.screen.fill(self.BGcolor)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        return 0

            self.data = read()
            text(self.screen, f"Games Played: {self.data['Games']}", 32, "MinecraftBold.otf", [0,0,0], 306, 100)
            text(self.screen, f"Rounds Played: {self.data['Rounds']}", 32, "MinecraftBold.otf", [0,0,0], 306, 200)
            text(self.screen, f"Highest Score: {self.data['Highest']}", 32, "MinecraftBold.otf", [0,0,0], 306, 300)
            text(self.screen, "Press ESC return to main menu", 32, "MinecraftBold.otf", [0,0,0], 306, 500)

            pygame.display.flip()
            self.Clock.tick(self.FPS)