from BrownianTreeSnowflake.particle import Particle
import pygame
import GraphicEngine
from typing import List


class Window(GraphicEngine.PygameGFX):
    listOfAngles: List[int]
    snowFlakes: List[List[Particle]]
    currents: List[Particle]

    @staticmethod
    def CreateParticle(width: int, height: int, angle: float) -> Particle:
        center = pygame.Vector2(width / 2, height / 2)

        startPosition = pygame.Vector2(width / 2, 0).rotate(angle)
        startPosition.x += width / 2
        startPosition.y += height / 2
        particle = Particle(startPosition.x, startPosition.y, center, angle)
        return particle

    def Setup(self) -> None:
        self.listOfAngles: List[int] = range(0, 360, 22)
        self.snowFlakes: List[Particle] = []
        self.currents: List[Particle] = []
        for i in range(len(self.listOfAngles)):
            self.currents.append(
                Window.CreateParticle(self.Width, self.Height, self.listOfAngles[i])
            )

    def Draw(self) -> None:
        self.background(r=0, g=0, b=0)
        for i in range(len(self.currents)):
            self.currents[i].update()
            self.currents[i].show(self.DisplaySurface)
            if self.currents[i].Finished | self.currents[i].Intersect(self.snowFlakes):
                if self.currents[i].WasValid:
                    self.snowFlakes.append(self.currents[i])
                    self.currents[i] = Window.CreateParticle(
                        self.Width, self.Height, self.listOfAngles[i]
                    )
                else:
                    self.currents[i].disable()
            for particle in self.snowFlakes:
                particle.show(self.DisplaySurface)
