from dataclasses import dataclass
import math
from typing import List
import GraphicEngine
import pygame


class Window(GraphicEngine.PygameGFX):
    axiom = "F"
    sentence = axiom
    angleDif = math.radians(25)
    length = 150
    rules = {
        "F": "FF+[+F-F-F]-[-F+F+F]",
    }

    def Setup(self):
        self.background(51)

    def Draw(self):
        self.turtle()
        # self.drawText(self.sentence, (255, 255, 255))

    def generate(self):
        nextSentence = ""
        for i in range(len(self.sentence)):
            current = self.sentence[i]
            if current in [x for x in self.rules]:
                nextSentence += self.rules[current]
            else:
                nextSentence += current
        self.length *= 0.5
        self.sentence = nextSentence

    def turtle(self):
        def getendPoz():
            x = math.cos(angle) * self.length
            y = math.sin(angle) * self.length
            return pygame.Vector2(x + startPoz.x, y + startPoz.y)

        def drawLine():
            pygame.draw.line(
                self.DisplaySurface, (255, 255, 255), startPoz, getendPoz()
            )

        startPoz = pygame.Vector2(self.Width / 2, self.Height)
        angle = -math.pi / 2
        memory: List[MemoryData] = []
        for char in self.sentence:
            match char:
                case "F":
                    drawLine()
                    startPoz = getendPoz()
                case "+":
                    angle += self.angleDif
                case "-":
                    angle -= self.angleDif
                case "[":
                    memory.append(MemoryData(startPoz, angle))
                case "]":
                    memData = memory.pop()
                    startPoz = memData.startPoz
                    angle = memData.angle
                case _:
                    pass

    def mouseReleased(self):
        self.generate()


@dataclass(slots=True)
class MemoryData:
    startPoz: pygame.Vector2
    angle: float
