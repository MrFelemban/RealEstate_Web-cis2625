#Snake Game code
import pygame as pg
import sys
from random import randrange

vec2 = pg.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.range = self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100  # milliseconds
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        
    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions[pg.K_w] = 1
                self.directions[pg.K_s] = 0
                self.directions[pg.K_a] = 1
                self.directions[pg.K_d] = 1

            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                self.directions[pg.K_w] = 0
                self.directions[pg.K_s] = 1
                self.directions[pg.K_a] = 1
                self.directions[pg.K_d] = 1

            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions[pg.K_w] = 1
                self.directions[pg.K_s] = 1
                self.directions[pg.K_a] = 1
                self.directions[pg.K_d] = 0

            if event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions[pg.K_w] = 1
                self.directions[pg.K_s] = 1
                self.directions[pg.K_a] = 0
                self.directions[pg.K_d] = 1


    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def get_random_position(self):
        return [randrange(*self.range), randrange(*self.range)]

    def check_borders(self):
        # Check if the snake hits the borders of the screen
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()

    def check_food(self):
        # Check if the snake hits the food
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1

    def check_selfeating(self):
        # Check if the snake hits itself
        for segment in self.segments[1:]:  # Skip the head
          if self.rect.colliderect(segment):
                self.game.new_game()
                break

