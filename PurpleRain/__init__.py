from typing import List
import GraphicEngine
from PurpleRain.drop import Drop


class Window(GraphicEngine.PygameGFX):
    drops: List[Drop]

    def Setup(self):
        self.drops = []
        for _ in range(500):
            self.drops.append(Drop(self.Width, self.Height))

    def Draw(self):
        self.background((230, 230, 250))
        for drop in self.drops:
            drop.update()
            drop.show(self.DisplaySurface)
