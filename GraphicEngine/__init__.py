from __future__ import annotations
from typing import Optional, Tuple
from abc import ABC, abstractmethod
import pygame


def drawPixel(surface: pygame.Surface, color: pygame.Color, pos: Tuple[int, int]):
    surface.set_at(pos, color)


def mathMap(x: float, in_min: float, in_max: float, out_min: float, out_max: float):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def constrain(value: float, lowLimit: float, highLimit: float):
    if value <= lowLimit:
        return lowLimit
    if value >= highLimit:
        return highLimit
    return value


class PygameGFX(ABC):
    __height: int
    __width: int
    __initHandle: Tuple[int, int]
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
        width: int,
        height: int,
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

    def Run(self):
        pygame.init()
        FramePerSec = pygame.time.Clock()
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
