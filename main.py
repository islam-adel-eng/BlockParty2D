from screens.main_menu import *
from screens.Game import *
from screens.GameOver import *
from screens.stats import *
import sys

icon = pygame.image.load(path("Resources/Images/icon.png"))
pygame.display.set_icon(icon)

menu = menu()
stats = stats()
game = game()
game_over = game_over(menu.Resolution)


Running = True
screen = 0

while Running:
    match screen:
        case 0:
            match menu.loop():
                case 0:
                    sys.exit()
                case 1:
                    screen = 1
                case 2:
                    screen = 3
                    
        case 1:
            if game.loop() == 0:
                screen = 2
        case 2:
            match game_over.loop():
                case 0:
                    screen = 1
                case 1:
                    screen = 0
        case 3:
            match stats.loop():
                case 0:
                    screen = 0
