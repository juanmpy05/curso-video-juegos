"""
This module was autogenerated by gale.
"""
import settings
from src.Rancexstreet import Rancexstreet

if __name__ == "__main__":
    game = Rancexstreet(
        "Rancexstreet",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
    )
    game.exec()
