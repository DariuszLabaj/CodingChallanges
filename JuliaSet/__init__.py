import GraphicEngine
import time
from math import sqrt


class Window(GraphicEngine.PygameGFX):
    n = 40
    cx = -0.70176
    cy = -0.3842

    def Setup(self):
        self.setCanvasSize(640, 480)

    def Draw(self):
        # self.cx = GraphicEngine.mathMap(self.mousePosition[0], 0, self.Width, -1, 1)
        # self.cy = GraphicEngine.mathMap(self.mousePosition[0], 0, self.Height, -1, 1)
        startTime = time.time()
        pixels = self.calculateSet(self.n, 4)
        for i in range(self.Width):
            for j in range(self.Height):
                self.drawShapes.Pixel(
                    self.DisplaySurface,
                    pixels[i][j],
                    (i, j)
                )
        self.drawShapes.Text(
            self.DisplaySurface,
            self.Font,
            f"Iterations : {self.n} | {time.time()-startTime:.03f} [s]",
            (51, 51, 51),
        )
        self.n += 1

    def calculateSet(self, noOfIterations: int, infinityMark: int):
        pixels: list[list[tuple[int, int, int]]] = [[(0, 0, 0) for _ in range(self.Height)] for __ in range(self.Width)]
        for i in range(self.Width):
            for j in range(self.Height):
                a = GraphicEngine.mathMap(i, 0, self.Width, -1.5, 1.5)
                b = GraphicEngine.mathMap(j, 0, self.Height, -1.5, 1.5)
                x = self.cx
                y = self.cy
                iterations = 0

                for n in range(noOfIterations):
                    aa = a * a
                    bb = b * b
                    if (aa + bb) > infinityMark:
                        break
                    two_ab = 2.0 * a * b
                    a = aa - bb + x
                    b = two_ab + y
                    iterations = n
                red = GraphicEngine.mathMap(iterations, 0, noOfIterations, 0, 1)
                red = GraphicEngine.mathMap(sqrt(red), 0, 1, 255, 0)
                if iterations == noOfIterations - 1:
                    red = 0
                pixels[i][j] = (int(red), int(red), int(red))
        return pixels
