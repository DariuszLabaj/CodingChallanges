from typing import Tuple
import GraphicEngine
import pygame
from TheSnakeGame.food import Food
from TheSnakeGame.snake import Snake


class Window(GraphicEngine.PygameGFX):
    player: Snake
    scale: int
    boundryX: Tuple[int, int]
    boundryY: Tuple[int, int]

    def keyPressed(self):
        match self.keyCode:
            case pygame.K_UP:
                self.player.dir(0, -1)
            case pygame.K_DOWN:
                self.player.dir(0, 1)
            case pygame.K_LEFT:
                self.player.dir(-1, 0)
            case pygame.K_RIGHT:
                self.player.dir(1, 0)

    def Setup(self):
        self.scale = 20
        self.boundryX = (0, self.Width-self.scale)
        self.boundryY = (0, self.Height-self.scale)
        self.player = Snake(self.scale, self.boundryX, self.boundryY)
        self.food = Food(self.scale, self.boundryX, self.boundryY)

    def FoodEaten(self):
        self.food = Food(self.scale, self.boundryX, self.boundryY)

    def Draw(self):
        self.background(51)
        self.food.show(self.DisplaySurface)
        self.player.update()
        self.player.show(self.DisplaySurface)
        if self.player.eat(self.food.getRect):
            self.FoodEaten()
