from __future__ import annotations
from typing import Optional, Tuple
from abc import ABC, abstractmethod
import pygame
from GraphicEngine.constrain import constrain
from GraphicEngine.mathMap import mathMap
from GraphicEngine.random2DVector import random2DVector


def drawPixel(surface: pygame.Surface, color: pygame.Color, pos: Tuple[int, int]):
    surface.set_at(pos, color)


class PygameGFX(ABC):
    __height: int
    __width: int
    __mousePosition: Tuple[int, int]
    __displaySufrace: pygame.Surface
    __running: bool
    __fps: int
    __keyCode: int

    @property
    def DisplaySurface(self):
        return self.__displaySufrace

    @property
    def FramePerSec(self):
        return pygame.time.Clock()

    @property
    def Width(self):
        return self.__width

    @property
    def Height(self):
        return self.__height

    @property
    def IsRunning(self):
        return self.__running

    @property
    def keyCode(self) -> int:
        return self.__keyCode

    @property
    def mousePosition(self):
        return self.__mousePosition

    def __init__(
        self,
        width: int = 400,
        height: int = 400,
        caption: Optional[str] = None,
        fps: Optional[int] = None,
    ) -> None:
        self.__running = True
        self.__height = height
        self.__width = width
        self.__displaySufrace = pygame.display.set_mode(
            (self.__width, self.__height), pygame.SRCALPHA
        )
        self.__fps = fps
        if caption:
            pygame.display.set_caption(caption)

    def _checkForEvents(self):
        events = pygame.event.get()
        for event in events:
            match event.type:
                case pygame.QUIT:
                    self.__running = False
                case pygame.KEYDOWN:
                    self.__keyCode = event.key
                    self.keyPressed()
                case pygame.KEYUP:
                    self.__keyCode = event.key
                    self.keyReleased()
                case pygame.MOUSEBUTTONDOWN:
                    self.__mousePosition = pygame.mouse.get_pos()
                    self.mousePressed()
                case pygame.MOUSEBUTTONUP:
                    self.__mousePosition = pygame.mouse.get_pos()
                    self.mouseReleased()

    def setCanvasSize(self, width: int, height: int):
        self.__height = height
        self.__width = width
        self.__displaySufrace = pygame.display.set_mode(
            (self.__width, self.__height), pygame.SRCALPHA
        )

    def Run(self):
        pygame.init()
        FramePerSec = pygame.time.Clock()
        self.__font = pygame.font.SysFont(None, 24)
        self.Setup()
        while self.IsRunning:
            self._checkForEvents()
            self.Draw()
            pygame.display.update()
            if self.__fps:
                FramePerSec.tick(self.__fps)

    def background(self, r: int, g: int = None, b: int = None):
        if r and g and b:
            self.__displaySufrace.fill((r, g, b))
        else:
            self.__displaySufrace.fill((r, r, r))

    def drawText(self, text: str, color: pygame.Color):
        self.DisplaySurface.blit(self.__font.render(text, True, color), (20, 20))

    def drawPixel(self, color: pygame.Color, pos: Tuple[int, int]):
        self.DisplaySurface.set_at(pos, color)

    def drawArc(
        self,
        rect: pygame.Rect,
        color: pygame.Color,
        startAngle: float,
        stopAngle: float,
        width: int = 1,
    ):
        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.arc(
            surface, color, surface.get_rect(), startAngle, stopAngle, width
        )
        self.DisplaySurface.blit(surface, rect)

    def drawCircle(
        self, center: pygame.Vector2, radius: float, color: pygame.Color, width: int = 0
    ):
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (radius, radius), radius, width)
        self.DisplaySurface.blit(surface, (center.x - radius, center.y - radius))

    def drawEllipse(self, rect: pygame.Rect, color: pygame.Color, width: int = 0):
        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.ellipse(
            surface, color, pygame.Rect(0, 0, rect.size[0], rect.size[1]), width
        )
        self.DisplaySurface.blit(surface, rect)

    def drawLine(
        self,
        startPos: pygame.Vector2,
        endPos: pygame.Vector2,
        color: pygame.Color,
        width: int = 1,
    ):
        rectWidth = abs(startPos.x - endPos.x)
        rectHeight = abs(startPos.y - endPos.y)
        if rectWidth == 0:
            rectWidth = 1
        if rectHeight == 0:
            rectHeight = 1
        surface = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
        pygame.draw.line(surface, color, (0, 0), (surface.get_rect().size), width)
        self.DisplaySurface.blit(surface, startPos)

    def drawPolygon(self):
        raise NotImplementedError()

    def drawRect(
        self,
        rect: pygame.Rect,
        color: pygame.Color,
        width: int = 0,
        borderRadius: int = -1,
        borderTopLeftRadius: int = -1,
        borderTopRightRadius: int = -1,
        borderBottomLeftRadius: int = -1,
        borderBottmRightRadius: int = -1,
    ):
        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            surface,
            color,
            pygame.Rect(0, 0, rect.width, rect.height),
            width,
            borderRadius,
            borderTopLeftRadius,
            borderTopRightRadius,
            borderBottomLeftRadius,
            borderBottmRightRadius,
        )
        self.DisplaySurface.blit(surface, rect)

    def keyPressed(self):
        pass

    def keyReleased(self):
        pass

    def mousePressed(self):
        pass

    def mouseReleased(self):
        pass

    @abstractmethod
    def Setup(self):
        print(f"{__name__}\\Setup test")

    @abstractmethod
    def Draw(self):
        print(f"{__name__}\\Draw test")


if __name__ == "__main__":
    help(constrain)
    help(mathMap)
    help(random2DVector)
