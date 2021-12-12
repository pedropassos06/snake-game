import random
import pygame
from time import sleep

class SnakeGame:

    def __init__(self):
        #initialize all pygame modules
        pygame.init()
        
        #ensure desirable setup
        self.width, self.height = 750, 750

        #colors
        self.orange = (255, 165, 0)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)

        #game is on
        self.gameON = True

        #define snake speed
        self.speed = 30

    def setup_screen(self):
        
        #title of screen
        pygame.display.set_caption("Snake Game by @PedroPassos")
        
        #setup screen
        s = pygame.display.set_mode((self.width, self.height))
        
        #update screen
        pygame.display.update()
        
        #start clock
        clock = pygame.time.Clock()

        return s, clock

    def initial_conditions(self):
        #initial coordinates
        x, y = 350, 350

        #intial increments set to 0
        x_increment, y_increment = 0, 0

        return x, y, x_increment, y_increment

    def directions(self, key):
        
        if key == pygame.K_DOWN:
            y_increment = 10
            x_increment = 0
        elif key == pygame.K_UP:
            y_increment = -10
            x_increment = 0
        elif key == pygame.K_LEFT:
            x_increment = -10
            y_increment = 0
        elif key == pygame.K_RIGHT:
            x_increment = 10
            y_increment = 0

        return x_increment, y_increment

    def out_of_bounds(self, x, y):

        return x >= self.width or y >= self.height or x <= 0 or y <= 0

    def game_over(self, color, screen):
        font_style = pygame.font.SysFont(None, 50)
        message = font_style.render("Game Over", True, color)
        screen.blit(message, [0.5*self.width, 0.5*self.height])

    def play(self):

        s, clock = self.setup_screen()

        x, y, x_increment, y_increment = self.initial_conditions()

        while self.gameON:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.gameON = False
                
                elif event.type == pygame.KEYDOWN:
                    
                    x_increment, y_increment = self.directions(event.key)
            
            if self.out_of_bounds(x, y):
                break

            x += x_increment
            y += y_increment

            s.fill(self.black)
            
            pygame.draw.rect(s, self.orange, [x, y, 25, 25])

            pygame.display.update()

            clock.tick(self.speed)

        self.game_over(self.blue, s)
        pygame.display.update()
        sleep(2)

        pygame.quit()
        quit()

    



game = SnakeGame()
game.play()