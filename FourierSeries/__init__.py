from math import cos, pi, sin
import GraphicEngine


class Window(GraphicEngine.PygameGFX):
    time: float = 0
    wave: list[float] = []

    def Setup(self):
        self.background(0)

    def Draw(self):
        self.background(61)
        self.translate(150, 200)

        x = 0
        y = 0
        radius = 0

        for i in range(3):
            prevX = x
            prevY = y
            n = i * 2 + 1
            radius = 75 * (4 / (n * pi))
            x += radius * cos(n * self.time)
            y += radius * sin(n * self.time)

            self.stroke((255, 255, 255))
            self.noFill()
            self.ellipse((prevX, prevY, radius*2, radius*2))

            # self.fill((255, 255, 255))
            # self.circle((x, y), 4)
            self.line((prevX, prevY), (x, y))

        self.wave.insert(0, y)
        self.translate(200, 0)
        self.line((x - 200, y), (0, self.wave[0]))
        self.noFill()
        self.polygon(
            [(i, x) for i, x in enumerate(self.wave)]
        )

        if (len(self.wave) > 250):
            self.wave.pop()

        self.time += 0.05
