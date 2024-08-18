import sys

import Fireworks
import FractalTreesLSystem
import FractalTreesRecursive
import FractalTreesSpaceColonization
import JuliaSet
import MandelbrotSet
import Metaballs
import ObjectOrientedFractalTrees
import PerlinNoiseFlowField
import Starfield
import TheSnakeGame
import PurpleRain
import SpaceInvadersClone
import MitosisSimulation
import MazeGenerator
import ReactionDiffusionAlgorithm
import MathematicalRosePatterns
import BrownianTreeSnowflake


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[1].isdigit():
        challenge = int(args[1])
    else:
        challenge = 10
    match challenge:
        case 1:
            window = Starfield.Window(
                800, 800, f"Coding Challenge #{challenge}: Starfield", 60
            )
        case 3:
            window = TheSnakeGame.Window(
                600, 600, f"Coding Challenge #{challenge}: The Snake Game", 10
            )
        case 4:
            window = PurpleRain.Window(
                640, 360, f"Coding Challenge #{challenge}: Purple Rain", 60
            )
        case 5:
            window = SpaceInvadersClone.Window(
                600, 400, f"Coding Challenge #{challenge}: Space Invaders", 60
            )
        case 6:
            window = MitosisSimulation.Window(
                600, 600, f"Coding Challenge #{challenge}: Mitosis Simulation", 60
            )
        case 10:
            window = MazeGenerator.Window(
                800, 800, f"Coding Challenge #{challenge}: Maze Generator"
            )
        case 13:
            window = ReactionDiffusionAlgorithm.Window(
                200, 200, f"Coding Challenge #{challenge}: Reaction Diffusion Algorithm"
            )
        case 14:
            window = FractalTreesRecursive.Window(
                600, 600, f"Coding Challenge #{challenge}: Fractal Trees Recursive", 60
            )
        case 15:
            window = ObjectOrientedFractalTrees.Window(
                600,
                600,
                f"Coding Challenge #{challenge}: Object Oriented Fractal Trees",
                60,
            )
        case 16:
            window = FractalTreesLSystem.Window(
                600, 600, f"Coding Challenge #{challenge}: Fractal Trees - L-System", 60
            )
        case 17:
            window = FractalTreesSpaceColonization.Window(
                600,
                600,
                f"Coding Challenge #{challenge}: Fractal Trees - Space Colonization",
                60,
            )
        case 21:
            window = MandelbrotSet.Window(
                width=640,
                height=480,
                caption=f"Coding Challenge #{challenge}: Mandelbrot Set",
                fps=60,
            )
        case 22:
            window = JuliaSet.Window(
                width=640,
                height=480,
                caption=f"Coding Challenge #{challenge}: Julia Set",
                fps=60,
            )
        case 24:
            window = PerlinNoiseFlowField.Window(
                width=340,
                height=280,
                caption=f"Coding Challenge #{challenge}: Perlin Noise Flow Field",
                fps=60,
            )
        case 27:
            window = Fireworks.Window(
                width=2200,
                height=1080,
                caption=f"Coding Challenge #{challenge}: Fireworks!",
                fps=120,
            )
        case 28:
            window = Metaballs.Window(
                width=150,
                height=150,
                caption=f"Coding Challenge #{challenge}: Metaballs",
            )
        case 55:
            window = MathematicalRosePatterns.Window(
                800,
                800,
                f"Coding Challenge #{challenge}: Mathematical Rose Patterns",
                60,
            )
        case 125:
            window = None
            text = f"Coding Challenge #{challenge}: Fourier Series"
        case 127:
            window = BrownianTreeSnowflake.Window(
                600, 600, f"Coding Challenge #{challenge}: Brownian Tree Snowflake"
            )
        case _:
            window = None
    if window:
        window.Run()
