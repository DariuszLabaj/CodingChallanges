from math import sqrt
import time
import GraphicEngine


class Window(GraphicEngine.PygameGFX):
    def Setup(self):
        self.setCanvasSize(240, 240)
        self.n = 1

    def Draw(self):
        startTime = time.time()
        self.calculateSet(self.n, 16)
        self.drawShapes.Text(
            self.DisplaySurface,
            self.Font,
            f"Iterations : {self.n} | {time.time()-startTime:.03f} [s]",
            (255, 255, 255),
        )
        self.n += 1

    def calculateSet(self, noOfIterations: int, infinityMark: int):
        for i in range(self.Width):
            for j in range(self.Height):
                a = GraphicEngine.mathMap(i, 0, self.Width, -1.5, 1.5)
                b = GraphicEngine.mathMap(j, 0, self.Height, -1.5, 1.5)
                x = a
                y = b
                iterations = 0

                for n in range(noOfIterations):
                    aa = a * a
                    bb = b * b
                    two_ab = 2.0 * a * b
                    if (aa + bb) > infinityMark:
                        break
                    a = aa - bb + x
                    b = two_ab + y
                    iterations = n
                red = abs(GraphicEngine.mathMap(abs(a + b), 0, 1000000, 0, 1))
                red = GraphicEngine.mathMap(sqrt(red), 0, 1, 0, 255)
                green = abs(GraphicEngine.mathMap(a, 0, 1000000, 0, 1))
                green = GraphicEngine.mathMap(sqrt(green), 0, 1, 0, 255)
                blue = abs(GraphicEngine.mathMap(b, 0, 1000000, 0, 1))
                blue = GraphicEngine.mathMap(sqrt(blue), 0, 1, 0, 255)
                self.drawShapes.Pixel(
                    self.DisplaySurface,
                    (
                        int((red * iterations) % 255),
                        int((green * iterations) % 255),
                        int((blue * iterations) % 255),
                    ),
                    (i, j),
                )
