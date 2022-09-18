from __future__ import annotations
from typing import Optional, Tuple
from abc import ABC, abstractmethod
import pygame


def drawPixel(surface: pygame.Surface, color: pygame.Color, pos: Tuple[int, int]):
    surface.set_at(pos, color)


def mathMap(x: float, in_min: float, in_max: float, out_min: float, out_max: float):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class PygameGFX(ABC):
    __height: int
    __width: int
    __initHandle: Tuple[int, int]
    __displaySufrace: pygame.Surface
    __running: bool
    __fps: int

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

    def __init__(
        self,
        width: int,
        height: int,
        caption: Optional[str] = None,
        fps: Optional[int] = None,
    ) -> None:
        self.__running = True
        self.__height = width
        self.__width = height
        self.__displaySufrace = pygame.display.set_mode(
            (self.__width, self.__height), pygame.SRCALPHA
        )
        self.__fps = fps
        if caption:
            pygame.display.set_caption(caption)

    def _checkForEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

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

    @abstractmethod
    def Setup(self):
        print(f"{__name__}\\Setup test")

    @abstractmethod
    def Draw(self):
        print(f"{__name__}\\Draw test")
