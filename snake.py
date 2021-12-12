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
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)

        #game is on
        self.gameON = True

        #game open
        self.gameRUNNING = True

        #define snake speed
        self.speed = 30

        #snake dimensions
        self.snake_size = 25

        #initialize snake
        self.snake = []

        #snake_length
        self.snake_length = 1

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
        x_coord, y_coord = 350, 350

        #intial increments set to 0
        x_increment, y_increment = 0, 0

        return x_coord, y_coord, x_increment, y_increment

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

    def out_of_bounds(self, x_coord, y_coord):

        return x_coord >= self.width or y_coord >= self.height or x_coord <= 0 or y_coord <= 0

    def write(self, color, screen, text):

        font_style = pygame.font.SysFont(None, 50)

        message = font_style.render(text, True, color)
        
        screen.blit(message, [0.5*self.width - 350, 0.5*self.height - 50])

    def draw_snake(self, snake_size, snake_list, s, color):
        for i in snake_list:
            pygame.draw.rect(s, color, [i[0], i[1], snake_size, snake_size])

    def play(self):

        s, clock = self.setup_screen()

        x_coord, y_coord, x_increment, y_increment = self.initial_conditions()

        foodx = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
        foody = round(random.randrange(0, self.height - self.snake_size) / 10.0) * 10.0

        while self.gameON:

            while not self.gameRUNNING:

                s.fill(self.black)

                self.write(self.white, s, "Game Over! Press (P) Play again or (Q) Quit")

                pygame.display.update()

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_q:
                            self.gameON = False
                            self.gameRUNNING = True

                        if event.key == pygame.K_p:
                            self.play()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.gameON = False
                
                elif event.type == pygame.KEYDOWN:
                    
                    x_increment, y_increment = self.directions(event.key)
            
            if self.out_of_bounds(x_coord, y_coord):
                self.gameRUNNING == False

            x_coord += x_increment
            y_coord += y_increment

            s.fill(self.black)
            
            pygame.draw.rect(s, self.green, [foodx, foody, self.snake_size, self.snake_size])

            self.snake_head = list()
            self.snake_head.append(x_coord)
            self.snake_head.append(y_coord)
            self.snake.append(self.snake_head)

            if len(self.snake) > self.snake_length:
                del self.snake[0]

            for x in self.snake[:-1]:
                if x == self.snake_head:
                    self.gameRUNNING = False

            self.draw_snake(self.snake_size, self.snake, s, self.orange)

            pygame.display.update()

            if x_coord == foodx and y_coord == foody:
                foodx = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
                foody = round(random.randrange(0, self.height - self.snake_size) / 10.0) * 10.0
                self.snake_length += 1
            
            clock.tick(self.speed)

        pygame.quit()
        quit()

    



game = SnakeGame()
game.play()