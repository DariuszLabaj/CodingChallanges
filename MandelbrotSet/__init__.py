from math import sqrt
import time
import GraphicEngine


class Window(GraphicEngine.PygameGFX):
    def Setup(self):
        self.setCanvasSize(240, 240)
        self.n = 1

    def Draw(self):
        startTime = time.time()
        self.calulateSet(self.n, 16)
        self.drawText(f"Iterations : {self.n} | {time.time()-startTime:.03f} [s]", (255, 255, 255))
        self.n += 1

    def calulateSet(self, noOfIterations: int, infinityMark: int):
        for x in range(self.Width):
            for y in range(self.Height):
                a = GraphicEngine.mathMap(x, 0, self.Width, -1.5, 1.5)
                b = GraphicEngine.mathMap(y, 0, self.Height, -1.5, 1.5)
                ca = a
                cb = b
                iterations = 0

                for n in range(noOfIterations):
                    aa = a * a - b * b
                    bb = 2 * a * b
                    a = aa + ca
                    b = bb + cb
                    if abs(a + b) > infinityMark:
                        break
                    iterations = n
                red = abs(GraphicEngine.mathMap(abs(a + b), 0, 1000000, 0, 1))
                red = GraphicEngine.mathMap(sqrt(red), 0, 1, 0, 255)
                green = abs(GraphicEngine.mathMap(a, 0, 1000000, 0, 1))
                green = GraphicEngine.mathMap(sqrt(green), 0, 1, 0, 255)
                blue = abs(GraphicEngine.mathMap(b, 0, 1000000, 0, 1))
                blue = GraphicEngine.mathMap(sqrt(blue), 0, 1, 0, 255)

                self.drawPixel(
                    (
                        (red * iterations) % 255,
                        (green * iterations) % 255,
                        (blue * iterations) % 255,
                    ),
                    (x, y),
                )
