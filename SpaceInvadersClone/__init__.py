from typing import List
import pygame
import GraphicEngine
from SpaceInvadersClone.missile import Missile
from SpaceInvadersClone.ship import Ship
from SpaceInvadersClone.target import Target


class Window(GraphicEngine.PygameGFX):
    player: Ship
    playerDir: int
    targets: List[Target]
    missiles: List[Missile]
    framecounter: int

    def Setup(self):
        self.missiles = []
        self.playerDir = 0
        self.framecounter = 0
        self.player = Ship(self.Width, self.Height)
        self.targets = []
        for i in range(6):
            self.targets.append(Target(i * 80 + 70, 60, self.Width, self.Height))
        for i in range(6):
            self.targets.append(Target(i * 80 + 70, 140, self.Width, self.Height))
            self.targets[-1].dir *= -1
        for i in range(6):
            self.targets.append(Target(i * 80 + 70, 220, self.Width, self.Height))

    def Draw(self):
        self.background(51)
        for missile in self.missiles:
            missile.update()
            missile.show(self.DisplaySurface)
            for target in self.targets:
                if missile.hits(target.getRect):
                    self.missiles.pop(self.missiles.index(missile))
                    self.targets.pop(self.targets.index(target))
        self.player.move(self.playerDir)
        self.player.show(self.DisplaySurface)
        for target in self.targets:
            if self.framecounter and self.framecounter % 60 == 0:
                target.update()
            if target.getRect.bottom > self.Height:
                self.Setup()
            target.show(self.DisplaySurface)
        self.framecounter += 1

    def keyPressed(self):
        match self.keyCode:
            case pygame.K_RIGHT:
                self.playerDir = 1
            case pygame.K_LEFT:
                self.playerDir = -1
            case pygame.K_SPACE:
                self.missiles.append(
                    Missile(self.player.x + 2, self.player.y, self.Width, self.Height)
                )

    def keyReleased(self):
        match self.keyCode:
            case pygame.K_RIGHT:
                if self.playerDir == 1:
                    self.playerDir = 0
            case pygame.K_LEFT:
                if self.playerDir == -1:
                    self.playerDir = 0
