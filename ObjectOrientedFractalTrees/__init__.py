import math
from typing import List
import pygame
import GraphicEngine
from ObjectOrientedFractalTrees.branch import Branch
from ObjectOrientedFractalTrees.leaf import Leaf


class Window(GraphicEngine.PygameGFX):
    branches: List[Branch] = []
    leaves: List[Leaf] = []
    count: int = 0

    def Setup(self):
        root = Branch(
            pygame.Vector2(self.Width / 2, self.Height), self.Width / 3, -math.pi / 2
        )
        self.branches.append(root)

    def Draw(self):
        self.background(51)
        for branch in self.branches:
            branch.show(self.DisplaySurface)
        for leaf in self.leaves:
            leaf.show(self.DisplaySurface)
            leaf.fall()
            if leaf.poz.y > self.Height:
                self.leaves.pop(self.leaves.index(leaf))

    def mouseReleased(self):
        if self.count < 6:
            for i in range(len(self.branches) - 1, -1, -1):
                self.branches += self.branches[i].branch()
            self.count += 1
        else:
            for i in range(len(self.branches)):
                if not self.branches[i].finished:
                    self.leaves.append(
                        Leaf(
                            self.branches[i].endPoz.x, self.branches[i].endPoz.y
                        )
                    )
