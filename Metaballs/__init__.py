from random import randint
from typing import List
import pygame
import GraphicEngine
import numpy as np
from GraphicEngine.random2DVector import random2DVector


class Window(GraphicEngine.PygameGFX):
    def Setup(self):
        self.blobs: List[Blob] = []
        for _ in range(6):
            self.blobs.append(
                Blob(
                    randint(0, self.Width),
                    randint(0, self.Height),
                    self.Width,
                    self.Height,
                )
            )
        self.blobs = np.array(self.blobs, Blob)
        self.xs = np.array(range(self.Width), int)
        self.ys = np.array(range(self.Height), int)
        self.pixels: list[pygame.Vector2] = []
        for x in self.xs:
            for y in self.ys:
                self.pixels.append(pygame.Vector2(x, y))

    def Draw(self):
        print(int(self.FramePerSec.get_fps()), end="\r")
        for pixel in self.pixels:
            color = 0
            for blob in self.blobs:
                distance = pixel.distance_to(blob.pos)
                color += 50 * blob.r / distance if distance > 0 else 255
            self.drawPixel(color, (int(pixel.x), int(pixel.y)))
        """for x in self.xs:
            for y in self.ys:
                color = 0
                pos = pygame.Vector2(x, y)
                for blob in self.blobs:
                    distance = pos.distance_to(blob.pos)
                    color += 50 * blob.r / distance if distance > 0 else 255
                self.drawPixel(color, (int(pos.x), int(pos.y)))"""
        for blob in self.blobs:
            blob.update()


class Blob:
    def __init__(self, x: float, y: float, w: int, h: int):
        self.r = 40
        self.pos = pygame.Vector2(x, y)
        self.vel = random2DVector()
        self.vel *= randint(2, 5)
        self.canvasWidth = w
        self.canvasHeight = h

    def show(self, window: pygame.Surface):
        pygame.draw.ellipse(
            window,
            (0, 0, 0),
            pygame.Rect(
                self.pos.x - self.r, self.pos.y - self.r, self.r * 2, self.r * 2
            ),
            width=1,
        )

    def update(self):
        self.pos += self.vel
        if self.pos.x > self.canvasWidth or self.pos.x < 0:
            self.vel.x *= -1
        if self.pos.y > self.canvasHeight or self.pos.y < 0:
            self.vel.y *= -1
