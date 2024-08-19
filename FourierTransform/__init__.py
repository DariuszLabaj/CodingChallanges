from math import atan2, cos, pi, sin, sqrt
import numpy as np
import time

from attr import dataclass
from FourierTransform import drawing
import GraphicEngine


@dataclass
class FourierData:
    re: float
    im: float
    freq: float
    amp: float
    phase: float


class Window(GraphicEngine.PygameGFX):
    time: float = 0
    path: list[tuple[float, float]] = []
    signalY: list[float] = []
    signalX: list[float] = []
    signalPath: list[tuple[float, float]] = []
    fourierY: list[FourierData] = []
    fourierX: list[FourierData] = []
    skip = 4

    def Setup(self):
        self.background(0)
        self.signalX = [drawing.drawing[i].x for i in range(0, len(drawing.drawing), self.skip)]
        self.signalY = [drawing.drawing[i].y for i in range(0, len(drawing.drawing), self.skip)]
        self.signalPath = [(drawing.drawing[i].x, drawing.drawing[i].y)
                           for i in range(0, len(drawing.drawing), self.skip)]
        startCalculationTime = time.time()
        # self.fourierX = self.dft(self.signalX)
        # self.fourierY = self.dft(self.signalY)
        self.fourierX = self.fft(self.signalX)
        self.fourierY = self.fft(self.signalY)
        print(f"Total Calculation Time: {(time.time()-startCalculationTime)*1000:.3f} [ms]")
        self.fourierX.sort(reverse=True, key=lambda val: val.amp)
        self.fourierY.sort(reverse=True, key=lambda val: val.amp)

    def epicycle(self, x: float, y: float, rotation: float, fourier: list[FourierData]):
        self.stroke((255, 255, 255, 192))
        radius = 0
        for val in fourier:
            prevX = x
            prevY = y
            freq = val.freq
            radius = val.amp
            phase = val.phase
            x += radius * cos(freq * self.time + phase + rotation)
            y += radius * sin(freq * self.time + phase + rotation)
            self.noFill()
            self.ellipse((prevX, prevY, radius*2, radius*2))
            self.line((prevX, prevY), (x, y))
        return x, y

    def Draw(self):
        self.background(40)
        # self.translate(150, 200)

        x1, y1 = self.epicycle(self.Width/2+100, 100, 0, self.fourierX)
        x2, y2 = self.epicycle(100, self.Height/2+80, (pi/2), self.fourierY)

        self.path.insert(0, (x1, y2))

        # self.translate(200, 0)
        self.stroke((255, 255, 255, 40))
        self.line((x1, y1), (self.path[0][0], self.path[0][1]))
        self.line((x2, y2), (self.path[0][0], self.path[0][1]))
        self.noFill()
        self.push()
        self.translate(500, 380)
        self.stroke((0, 255, 255, 60))
        self.polygon(self.signalPath)
        self.pop()
        self.stroke((255, 255, 255, 255))
        self.polygon(self.path)
        if (len(self.path) > len(drawing.drawing)/self.skip-10):
            self.path.pop()

        dt = (pi*2)/len(self.fourierY)
        self.time += dt

    @staticmethod
    def dft(x: list[float]) -> list[FourierData]:
        N = len(x)
        X: list[FourierData] = [FourierData(0, 0, 0, 0, 0) for _ in range(N)]
        for k in range(N):
            re = 0.0
            im = 0.0
            for n in range(N):
                phi = ((2*pi)*k*n)/N
                re += x[n]*cos(phi)
                im -= x[n]*sin(phi)
            re = re / N
            im = im / N
            freq = k
            amp = sqrt(re*re+im*im)
            phase = atan2(im, re)
            X[k] = FourierData(re, im, freq, amp, phase)
        return X

    @staticmethod
    def fft(x: list[float]) -> list[FourierData]:
        N = len(x)
        X_complex = np.fft.fft(x)
        X = [
            FourierData(
                re=np.real(X_complex[k])/N,
                im=np.imag(X_complex[k])/N,
                freq=k,
                amp=np.abs(X_complex[k])/N,
                phase=np.angle(X_complex[k])
            )
            for k in range(N)
        ]
        return X
