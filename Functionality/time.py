import time
import pygame
from Functionality.image import *
from Objects.UI import *

def delta_time(last_time, FPS):
    dt = time.time() - last_time
    dt *= FPS
    last_time = time.time()

    return [dt, last_time]

class Timer():
    def __init__(self, time, tick_bool):
        self.time = time
        self.last_time = pygame.time.get_ticks()
        self.counted = 0
        self.tick = pygame.mixer.Sound(path("Resources/Audio/tick.mp3"))
        self.tick_channel = pygame.mixer.Channel(0)
        self.tick_bool = tick_bool

    def count(self):
        if pygame.time.get_ticks() - self.last_time > 1000:
            if self.time - self.counted > 0 and self.tick_bool == True:
                self.tick_channel.play(self.tick)
            self.counted += 1
            self.last_time = pygame.time.get_ticks()

        return int(self.time - self.counted)

    def reset(self):
        self.counted = 0

class PreRound(Timer):
    def __init__(self, time, tick_bool):
        super().__init__(time, tick_bool)
    def count(self):
        return super().count()
    def reset(self):
        return super().reset()
    
    def execute(self):
            #self.start_sound.play(0)
            self.reset()
            return 1 # Next round state

class Round(Timer):
    def __init__(self, time, tick_bool):
        super().__init__(time, tick_bool)
    def count(self):
        return super().count()
    def reset(self):
        return super().reset()
    
    def execute(self, player_color, color):
        if player_color == color:
            won = True
        else:
            won = False
        self.reset()
        return [2, won]

    