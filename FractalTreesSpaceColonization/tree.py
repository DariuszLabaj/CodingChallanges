from typing import List, Tuple
from FractalTreesSpaceColonization.branch import Branch

from FractalTreesSpaceColonization.leaf import Leaf
import pygame


class Tree:
    maxDist = 30
    minDist = 15

    def __init__(self, canvasDimmensions: Tuple[int, int]):
        self.leaves: List[Leaf] = []
        self.branches: List[Branch] = []

        for _ in range(1500):
            self.leaves.append(Leaf(canvasDimmensions))
        dir = pygame.Vector2(0, -1)
        self.root = Branch(
            None, pygame.Vector2(canvasDimmensions[0] / 2, canvasDimmensions[1]), dir
        )
        self.branches.append(self.root)
        current = self.root
        found = False
        while not found:
            for leaf in self.leaves:
                distance = current.pos.distance_to(leaf.pos)
                if distance < self.maxDist:
                    found = True
                    break
            if not found:
                branch = current.next()
                current = branch
                self.branches.append(branch)

    def show(self, window: pygame.Surface):
        for leaf in self.leaves:
            leaf.show(window)
        for branch in self.branches:
            branch.show(window)

    def grow(self):
        for leaf in self.leaves:
            closestBranch = None
            record = 100_000
            for branch in self.branches:
                distance = leaf.pos.distance_to(branch.pos)
                if distance < self.minDist:
                    leaf.reched = True
                    closestBranch = None
                    break
                elif distance > self.maxDist:
                    continue
                elif closestBranch is None or distance < record:
                    closestBranch = branch
                    record = distance
            if closestBranch is not None:
                newDir = leaf.pos - closestBranch.pos
                newDir = newDir.normalize()
                closestBranch.dir += newDir
                closestBranch.dir = closestBranch.dir.normalize()
                closestBranch.count += 1
        for i in range(len(self.leaves) - 1, -1, -1):
            if self.leaves[i].reched:
                self.leaves.pop(i)

        for i in range(len(self.branches)-1, -1, -1):
            if self.branches[i].count > 0:
                self.branches[i].dir /= self.branches[i].count+1
                self.branches.append(self.branches[i].next())
            self.branches[i].reset()
