import sys
import Starfield
import TheSnakeGame
import PurpleRain
import SpaceInvadersClone
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
    if window:
        window.Run()
