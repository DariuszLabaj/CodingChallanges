from FractalTreesSpaceColonization.tree import Tree
import GraphicEngine


class Window(GraphicEngine.PygameGFX):
    def Setup(self):
        self.tree = Tree((self.Width, self.Height))

    def Draw(self):
        self.background(51)
        self.tree.show(self.DisplaySurface)
        self.tree.grow()
