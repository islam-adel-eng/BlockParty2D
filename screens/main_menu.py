import pygame, sys
from Objects.UI import *
from Objects.Player import *
from Functionality.data import *
import vars

class menu():
    def __init__(self):
        pygame.init()
        self.music = pygame.mixer.Sound(path("Resources\Audio\menu_music.mp3"))
        self.music.set_volume(0.5)

        self.music_channel = pygame.mixer.Channel(2)
        
        # Screen variables
        #self.Resolution = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.Resolution = [612, 612] # x = 512, y = 512 
        self.screen = pygame.display.set_mode(self.Resolution)
        self.BG_color = [0,0,0]

        # Time variables
        self.Clock = pygame.time.Clock()
        self.FPS = 60

        # Loop variables
        self.Running = True

        # define buttons
        self.Button1 = button(self.screen, [255,255,255],[300, 50], [self.Resolution[0]/2, self.Resolution[1]/2], "START", 0, 1, 0, False, ["Button1.png", "Button1-2.png"])
        self.Button2 = button(self.screen, [255,255,255],[250, 50], [self.Resolution[0]/2, self.Resolution[1]/2 + 75], "STATS", 0, 2, 0, False,["Button2.png", "Button2-2.png"])
        self.Button3 = button(self.screen, None, [18, 18], [self.Resolution[0]-36, self.Resolution[1]-36], "", 0, 0, 0, False, ["unmuted.png", "unmuted-hover.png"])
        self.Buttons = [self.Button1, self.Button2]

        self.title = pygame.image.load(path("Resources/Images/Title.png"))
        self.title.set_colorkey([255,255,255])
        self.title_rect = self.title.get_rect()
        self.title_rect.center = [self.Resolution[0]/2, 150]

        

    def loop(self):
        pygame.display.set_caption("Main Menu")
        self.music_channel.play(self.music, -1, fade_ms=2000)
        while self.Running:

            if vars.toggle_music == True:
                self.music_channel.unpause()
                self.Button3.image = ["unmuted.png", "unmuted-hover.png"]

            if vars.toggle_music == False:
                self.Button3.image = ["muted.png", "muted-hover.png"]
                self.music_channel.pause()

            self.screen.fill([164,159,255])
            for i in self.Buttons:
                i.draw()
                i.hover()

            self.Button3.draw()
            self.Button3.hover()

            if pygame.mouse.get_pressed()[0]:
                for btn in self.Buttons:
                    if btn.state == 1:
                        self.music.stop()
                        return btn.result
            
                    

            self.screen.blit(self.title, self.title_rect, None)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    if self.Button3.state == 1:
                       vars.toggle_music = not vars.toggle_music


            pygame.display.flip()
            self.Clock.tick(self.FPS)
