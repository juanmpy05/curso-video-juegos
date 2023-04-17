"""
This module was autogenerated by gale.
"""
import pathlib

import pygame

from gale import frames
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")

# Size we want to emulate
VIRTUAL_WIDTH = 1280
VIRTUAL_HEIGHT = 720
# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BASE_DIR = pathlib.Path(__file__).parent

# Register your textures from the graphics folder, for instance:
# TEXTURES = {
#     'my_texture': pygame.image.load(BASE_DIR / "assets" / "graphics" / "my_texture.png")
# }
TEXTURES = {
    "road_0": pygame.image.load(BASE_DIR / "graphics" / "object" / "road_0.png"),
    "startstate":pygame.image.load(BASE_DIR / "graphics" / "startstate.png"),
}

# Register your frames, for instance:
# FRAMES = {
#     'my_frames': frames.generate_frames(TEXTURES['my_texture'], 16, 16)
# }
FRAMES = {}

pygame.mixer.init()

# Register your sound from the sounds folder, for instance:
# SOUNDS = {
#     'my_sound': pygame.mixer.Sound(BASE_DIR / "assets"  / "sounds" / "my_sound.wav"),
# }
SOUNDS = {}

pygame.font.init()

# Register your fonts from the fonts folder, for instance:
# FONTS = {
#     'small': pygame.font.Font(BASE_DIR / "assets"  / "fonts" / "font.ttf", 8)
# }
FONTS = {
    "tiny": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 16),
    "small": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 32),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 40),
    "mediumPlus": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 43),
    "large": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 50)

}
