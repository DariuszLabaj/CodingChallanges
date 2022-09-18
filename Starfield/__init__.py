from typing import List
import GraphicEngine
from Starfield.star import Star


class Window(GraphicEngine.PygameGFX):
    stars: List[Star]

    def Setup(self):
        self.stars = []
        for i in range(int(self.Width*self.Height/400)):
            self.stars.append(Star(self.Width, self.Height))

    def Draw(self):
        self.background(10)
        for star in self.stars:
            star.update()
            star.show(self.DisplaySurface)
