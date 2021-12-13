import random
import pygame
from time import sleep
from snake_helper import SnakeHelper

class SnakeGame(SnakeHelper):

    def __init__(self):
        super().__init__()

    def play(self):

        sh = SnakeHelper()
        s, clock = sh.setup_screen()

        x_coord, y_coord, x_increment, y_increment = sh.initial_conditions()

        foodx = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
        foody = round(random.randrange(0, self.height - self.snake_size) / 10.0) * 10.0

        while self.gameON:

            while not self.gameRUNNING:

                s.fill(self.black)

                sh.write(self.white, s, "Game Over! Press (P) Play again or (Q) Quit")

                pygame.display.update()

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_q:
                            self.gameON = False
                            self.gameRUNNING = False

                        if event.key == pygame.K_p:
                            self.play()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.gameON = False
                
                elif event.type == pygame.KEYDOWN:
                    
                    x_increment, y_increment = sh.directions(event.key)
            
            if sh.out_of_bounds(x_coord, y_coord):
                self.gameRUNNING == False

            x_coord += x_increment
            y_coord += y_increment

            s.fill(self.black)
            
            pygame.draw.circle(s, self.green, (foodx, foody),5)

            self.snake_head = list()
            self.snake_head.append(x_coord)
            self.snake_head.append(y_coord)
            self.snake.append(self.snake_head)

            if len(self.snake) > self.snake_length:
                del self.snake[0]

            for x in self.snake[:-1]:
                if x == self.snake_head:
                    self.gameRUNNING = False

            sh.draw_snake(self.snake_size, self.snake, s, self.orange)

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