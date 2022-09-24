import sys
import FractalTreesLSystem
import FractalTreesRecursive
import FractalTreesSpaceColonization
import ObjectOrientedFractalTrees
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
        challange = int(args[1])
    else:
        challange = 1
    match challange:
        case 1:
            window = Starfield.Window(
                800, 800, f"Coding Challange #{challange}: Starfield", 60
            )
        case 3:
            window = TheSnakeGame.Window(
                600, 600, f"Coding Challange #{challange}: The Snake Game", 10
            )
        case 4:
            window = PurpleRain.Window(
                640, 360, f"Coding Challange #{challange}: Purple Rain", 60
            )
        case 5:
            window = SpaceInvadersClone.Window(
                600, 400, f"Coding Challange #{challange}: Space Invaders", 60
            )
        case 6:
            window = MitosisSimulation.Window(
                600, 600, f"Coding Challange #{challange}: Mitosis Simulation", 60
            )
        case 10:
            window = MazeGenerator.Window(
                800, 800, f"Coding Challange #{challange}: Maze Generator"
            )
        case 13:
            window = ReactionDiffusionAlgorithm.Window(
                200, 200, f"Coding Challange #{challange}: Reaction Diffusion Algorithm"
            )
        case 14:
            window = FractalTreesRecursive.Window(
                600, 600, f"Coding Challange #{challange}: Fractal Trees Recursive", 60
            )
        case 15:
            window = ObjectOrientedFractalTrees.Window(
                600, 600, f"Coding Challange #{challange}: Object Oriented Fractal Trees", 60
            )
        case 16:
            window = FractalTreesLSystem.Window(
                600, 600, f"Coding Challange #{challange}: Fractal Trees - L-System", 60
            )
        case 17:
            window = FractalTreesSpaceColonization.Window(
                600, 600, f"Coding Challange #{challange}: Fractal Trees - Space Colonization", 60
            )
        case 55:
            window = MathematicalRosePatterns.Window(
                800,
                800,
                f"Coding Challange #{challange}: Mathematical Rose Patterns",
                60,
            )
        case 127:
            window = BrownianTreeSnowflake.Window(
                600, 600, f"Coding Challange #{challange}: Brownian Tree Sonwflake"
            )
        case _:
            window = None
    if window:
        window.Run()
