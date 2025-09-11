import pygame
import sys
from Objects.Player import *
from Objects.UI import *
from Functionality.time import *
from Functionality.image import *
from Functionality.data import *
import time
import vars

class game():
    def __init__(self):
        # Screen variables
        self.Original_Resolution = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        #self.Original_Resolution = [512, 512] 
        self.UI_h = 50
        self.Resolution = [self.Original_Resolution[0], self.Original_Resolution[1]+self.UI_h]
        self.screen = pygame.display.set_mode(self.Resolution)
        self.BG_color = [0,0,0]

        # Time variables
        self.Clock = pygame.time.Clock()
        self.FPS = 60
        self.last_time = time.time()

        # Rounds variables
        self.new_round = True
        self.Round = 1
        # Loop variables
        self.Running = True
        # Player object
        self.Player = player([255,255,255], 5, self.Original_Resolution[0]/2, self.Original_Resolution[1]/2, 1)

        self.round_state = 0

        self.image = None
        self.color = None
        self.won = None

        self.correct_sound = pygame.mixer.Sound(path("Resources/Audio/correct.mp3"))
        self.sounds_channel = pygame.mixer.Channel(1)

        self.music = pygame.mixer.Sound(path("Resources\\Audio\\menu_music.mp3"))
        self.music.set_volume(0.5)
        self.music_channel = pygame.mixer.Channel(2)

        self.PreRoundTimer = PreRound(4, True)
        self.RoundTimer = Round(8, False)

    def loop(self):
        if vars.toggle_music == True:
            self.music_channel.play(self.music, -1)
        self.Round = 1
        pygame.display.set_caption("Game")
        while self.Running:
            self.screen.fill(self.BG_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False
                    sys.exit()

            # framerate independence
            delta = delta_time(self.last_time, self.FPS)
            dt, self.last_time= delta[0], delta[1]
            

            if self.image and self.color != None:
                self.screen.blit(self.image, [0,self.UI_h], None)
                pygame.draw.rect(self.screen, self.color, pygame.Rect(0,0,self.Resolution[0], self.UI_h))
                pygame.draw.line(self.screen, [0,0,0], [-1, self.UI_h], [self.Resolution[0]+1, self.UI_h], 5)
            
            match self.won:
                case True:
                    self.sounds_channel.play(self.correct_sound)
                    self.Round += 1
                    self.won = None
                case False:
                    self.music_channel.stop()
                    self.data = read()
                    write({"Games":self.data["Games"]+1, "Rounds":self.data["Rounds"]+self.Round, "Highest":self.Round if self.Round >= self.data["Highest"] else self.data["Highest"]})
                    if self.Round > self.data["Highest"]:
                        vars.New_HS = True
                    else:
                        vars.New_HS = False
                    self.won = None
                    return 0
            
            match self.round_state:
                case 0:
                    self.music_channel.pause()
                    if self.new_round == True:
                        self.image, self.color = PickImage(self.Original_Resolution)
                        self.new_round = False
                        self.Text_Color = [self.color[0]/2 + 20,self.color[1]/2 + 20,self.color[2]/2 + 20]
                    
                    text(self.screen, f"STARTING IN: {self.PreRoundTimer.time-self.PreRoundTimer.counted}", 32, "MinecraftBold.otf", self.Text_Color, self.Resolution[0]/2, self.UI_h/2)
                    if self.PreRoundTimer.count() == -1:
                        self.round_state = self.PreRoundTimer.execute()
                case 1:
                    self.music_channel.unpause()
                    text(self.screen, f"{self.RoundTimer.time-self.RoundTimer.counted}", 32, "MinecraftBold.otf", self.Text_Color, self.Resolution[0]/2, self.UI_h/2)
                    if self.RoundTimer.count() == -1:
                        self.round_state, self.won = self.RoundTimer.execute(self.screen.get_at([int(self.Player.posX), int(self.Player.posY)]), self.color)
                case 2:
                    self.new_round = True
                    self.round_state = 0
                    

            text(self.screen, f"{self.Round}", 32, "MinecraftBold.otf", self.Text_Color, 50, self.UI_h/2)

            if self.screen.get_at([int(self.Player.posX), int(self.Player.posY)]) == [255,255,255]:
                self.Player.color = [0,0,0]
            else:
                self.Player.color = [255,255,255]

            self.Player.draw(self.screen, dt, self.UI_h+5, self.round_state)

            pygame.display.flip()
            self.Clock.tick(self.FPS)