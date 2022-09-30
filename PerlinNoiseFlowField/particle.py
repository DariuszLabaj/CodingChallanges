from typing import List
import pygame

import GraphicEngine


class Particle:
    pos: pygame.Vector2
    vel: pygame.Vector2
    acc = pygame.Vector2(0, 0)
    maxSpeed = 1.5

    def __init__(self, x: int, y: int, maxX: int, maxY: int):
        self.pos = pygame.Vector2(x, y)
        self.prevPos = pygame.Vector2(self.pos.x, self.pos.y)
        self.vel = GraphicEngine.random2DVector()
        self.maxX = maxX
        self.maxY = maxY

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        if self.vel.magnitude() > self.maxSpeed:
            self.vel.scale_to_length(self.maxSpeed)
        self.edges()

    def applyForce(self, force: pygame.Vector2):
        self.acc += force

    def follow(
        self, flowFiled: List[pygame.Vector2], colums: int, rows: int, size: int
    ):
        c = int(self.pos.x / size)
        r = int(self.pos.y / size)
        r1 = r if r < rows else rows - 1
        c1 = c if c < colums else colums - 1
        flowVectorIndex = r1 * rows + c1
        # print(flowVectorIndex, len(flowFiled), c1, r1, c, r)
        force = flowFiled[flowVectorIndex]
        self.applyForce(force)

    def show(self, window: pygame.Surface):
        surface = pygame.Surface((self.maxX, self.maxY), pygame.SRCALPHA)
        pygame.draw.line(surface, (0, 0, 0, 10), self.prevPos, self.pos)
        window.blit(surface, (0, 0))
        self.updatePrevous()

    def updatePrevous(self):
        self.prevPos.x = self.pos.x
        self.prevPos.y = self.pos.y

    def edges(self):
        if self.pos.x > self.maxX:
            self.pos.x = 0
            self.updatePrevous()
        if self.pos.x < 0:
            self.pos.x = self.maxX
            self.updatePrevous()
        if self.pos.y > self.maxY:
            self.pos.y = 0
            self.updatePrevous()
        if self.pos.y < 0:
            self.pos.y = self.maxY
            self.updatePrevous()
