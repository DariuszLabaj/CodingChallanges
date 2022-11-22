import random
from math import pi
from typing import List

import GraphicEngine
import pygame
from perlin_noise import PerlinNoise  # type: ignore

from PerlinNoiseFlowField.particle import Particle


def Vector2fromAngle(angle: float, amlitude: float = 10):
    newHeading = pygame.Vector2(amlitude, 0)
    newHeading.rotate_rad_ip(angle)
    return newHeading


class Window(GraphicEngine.PygameGFX):
    noise = PerlinNoise()
    inc = 0.3
    zinc = 0.01
    scale = 10
    zoff = 0
    particles: List[Particle]
    flowFiled: List[pygame.Vector2]

    def Setup(self):

        self.cols = int(self.Width / self.scale)
        self.rows = int(self.Height / self.scale)
        self.vectors: List[List[pygame.Vector2]] = []
        self.flowFiled: List[pygame.Vector2] = []
        for x in range(self.cols):
            self.vectors.append([])
            for y in range(self.rows):
                self.vectors[x].append(pygame.Vector2(x * self.scale, y * self.scale))
                self.flowFiled.append(pygame.Vector2())
        self.particles = []
        rng = random.Random()
        for _ in range(100):
            self.particles.append(
                Particle(
                    rng.randint(0, self.Width),
                    rng.randint(0, self.Height),
                    self.Width,
                    self.Height,
                )
            )
        self.noises: List[List[float]] = [
            [
                [
                    self.noise([x * self.inc, y * self.inc*0.1, z * self.zinc])
                    for x in range(self.cols)
                ]
                for y in range(self.rows)
            ]
            for z in range(int(1 / self.zinc))
        ]
        self.background(255)

    def Draw(self):
        # self.background(255)
        for x in range(self.cols):
            for y in range(self.rows):
                currentaAngle = GraphicEngine.mathMap(
                    self.noises[x][y][self.zoff % len(self.noises[x][y])],
                    -1,
                    1,
                    2*pi,
                    -2*pi,
                )
                vector = Vector2fromAngle(currentaAngle, 1)
                # vector.scale_to_length(0.1)
                self.flowFiled[x + y * self.rows] = vector
                # pygame.draw.line(self.DisplaySurface, (255,0,0), self.vectors[x][y], self.vectors[x][y]+vector*10)
        for particle in self.particles:
            particle.follow(self.flowFiled, self.cols, self.rows, self.scale)
            particle.update()
            particle.show(self.DisplaySurface)
        self.zoff += 1
        print(int(self.FramePerSec.get_fps()), end="\r")
