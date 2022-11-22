from random import randint
from typing import List, Tuple

import pygame
from Fireworks.particle import Particle
from GraphicEngine.hsvToRgb import hsvToRgb


class Firework:
    @property
    def offScreen(self) -> bool:
        return self.exploded and not self.particles

    def __getRandomColor(self) -> Tuple[int, int, int]:
        return hsvToRgb(randint(0, 359))

    def __init__(self, width: int, height: int, gravity: pygame.Vector2):
        self.canvasWidth = width
        self.canvasHeight = height
        self.gravity = gravity
        self.size = 2
        self.firework = Particle(
            randint(0, self.canvasWidth),
            self.canvasHeight,
            True,
            self.size,
            self.__getRandomColor(),
            height
        )
        self.exploded = False
        self.particles: List[Particle] = []

    def update(self):
        self.firework.applyForce(self.gravity)
        self.firework.update()
        if not self.exploded:
            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()
        for particle in self.particles:
            particle.applyForce(self.gravity)
            particle.update()
            if particle.done:
                self.particles.pop(self.particles.index(particle))

    def explode(self):
        self.particles = []
        for _ in range(100):
            self.particles.append(
                Particle(
                    self.firework.pos.x,
                    self.firework.pos.y,
                    False,
                    self.size,
                    self.firework.Color,
                )
            )

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        if not self.exploded:
            self.firework.show(window)
        for particle in self.particles:
            particle.show(window)
