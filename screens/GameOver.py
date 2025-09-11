import pygame
import random, sys
from Objects.UI import text
from Functionality.data import read
import vars

class game_over():
    def __init__(self, Resolution):
        self.Resolution = Resolution
        self.screen = pygame.display.set_mode(self.Resolution)
        self.BG_color = [0,0,0]

        self.Quotes = [
                        "Are you color blind?",
                        "Nice try!",
                        "Damn.",
                        "Skill issues",
                        "It's okay :)",
                        "How did you lose that?"
                      ]

        self.Clock = pygame.time.Clock()
        self.FPS = 60

        self.Running = True
    
    def loop(self):
        self.Quote = random.choice(self.Quotes)
        pygame.display.set_caption("Game Over")
        while self.Running:
            self.screen.fill(self.BG_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_r]:
                        return 0
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        return 1

            
            text(self.screen, "GAME OVER!", 72, "MinecraftBold.otf", [255,0,0], self.Resolution[0]/2, self.Resolution[1]/2 - 150)
            text(self.screen, self.Quote, 32, "MinecraftBold.otf", [255,255,255], self.Resolution[0]/2, self.Resolution[1]/2 - 100)
            text(self.screen, "Press ESC return to main menu", 32, "MinecraftBold.otf", [255,255,255], self.Resolution[0]/2, self.Resolution[1]/2 + 150)
            text(self.screen, "Press R to play again", 36, "MinecraftBold.otf", [255,255,255], self.Resolution[0]/2, self.Resolution[1]/2 + 200)

            if vars.New_HS == True:
                data = read()
                text(self.screen, f"NEW HIGHSCHORE! {data['Highest']}", 32, "MinecraftBold.otf", [0,255,0], self.Resolution[0]/2, self.Resolution[1]/2)
            pygame.display.flip()
            self.Clock.tick(self.FPS)
            
        