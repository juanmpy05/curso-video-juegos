"""
This module was autogenerated by gale.
"""
import pathlib

import pygame

from gale import frames
from gale import input_handler

from src.utilities.frames import (
    generate_icons_frames,
    generate_frames,
    generate_powerUp_frames,
)

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_q, "home")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_x, "powerup_1")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_z, "powerup_2")

# Size we want to emulate
VIRTUAL_WIDTH = 1280
VIRTUAL_HEIGHT = 720
# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

POWERUP_SPEED = 100
POWERUP_LIMIT_GHOST = 3
POWERUP_LIMIT_SLOWLY = 5

PLAYER_INITIAL_SPEED = 250
PLAYER_SPEED = PLAYER_INITIAL_SPEED
CAR_SPEED = [
    PLAYER_SPEED // 2,
    PLAYER_SPEED,
    PLAYER_SPEED // 2,
    PLAYER_SPEED // 2,
    PLAYER_SPEED // 2,
    PLAYER_SPEED // 2,
    PLAYER_SPEED // 4,
    PLAYER_SPEED // 2,
    PLAYER_SPEED // 5,
]
GENERATE_CAR = 1
NUM_SKIN = 9
NUM_VIAS = 4
POS_SET = [462, 575, 701, 822]
BASE_DIR = pathlib.Path(__file__).parent
ICON_HEIGHT = 81.8
ICON_WIDTH = 80.9
CAR_HEIGHT = 164
CAR_WIDTH = 75
NUM_HIGHSCORES = 7
LIST_POWERUP = ["Ghost", "Slowly"]
LIST_MAP = ["map1", "map2", "map3", "map4", "map5"]
NEXT_MAP = 10
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = (249, 154, 2)
COLOR_ORANGE_DARK = (240, 38, 10)
COLOR_LIGHT = (206, 173, 139)

TEXTURES = {
    "road_0_left": pygame.image.load(
        BASE_DIR / "graphics" / "object" / "road_0_left.png"
    ),
    "road_0_right": pygame.image.load(
        BASE_DIR / "graphics" / "object" / "road_0_right.png"
    ),
    "map1": pygame.image.load(BASE_DIR / "graphics" / "object" / "Soil_Tile1.png"),
    "map2": pygame.image.load(BASE_DIR / "graphics" / "object" / "Soil_Tile2.png"),
    "map3": pygame.image.load(BASE_DIR / "graphics" / "object" / "Soil_Tile3.png"),
    "map4": pygame.image.load(BASE_DIR / "graphics" / "object" / "Soil_Tile4.png"),
    "map5": pygame.image.load(BASE_DIR / "graphics" / "object" / "Soil_Tile5.png"),
    "background": pygame.image.load(BASE_DIR / "graphics" / "background.png"),
    "EscenaStar": pygame.image.load(BASE_DIR / "graphics" / "EscenaStar.png"),
    "EscenaSelect": pygame.image.load(BASE_DIR / "graphics" / "EscenaSelect.png"),
    "EscenaGameOver": pygame.image.load(BASE_DIR / "graphics" / "EscenaGameOver.png"),
    "cartel1": pygame.image.load(BASE_DIR / "graphics" / "cartel1.png"),
    "cartel2": pygame.image.load(BASE_DIR / "graphics" / "cartel2.png"),
    "cartel3": pygame.image.load(BASE_DIR / "graphics" / "cartel3.png"),
    "cartel4": pygame.image.load(BASE_DIR / "graphics" / "cartel4.png"),
    "cartel5": pygame.image.load(BASE_DIR / "graphics" / "cartel5.png"),
    "carSelectState": pygame.image.load(BASE_DIR / "graphics" / "carSelectState.png"),
    "startate": pygame.image.load(BASE_DIR / "graphics" / "startstate.png"),
    "icons": pygame.image.load(BASE_DIR / "graphics" / "icons.png"),
    "Set_vehicle0": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle.png"
    ),
    "Set_vehicle1": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle2.png"
    ),
    "Set_vehicle2": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle3.png"
    ),
    "Set_vehicle3": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle4.png"
    ),
    "Set_vehicle4": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle5.png"
    ),
    "Set_vehicle5": pygame.image.load(
        BASE_DIR / "graphics" / "vehicle" / "Set_vehicle6.png"
    ),
    "powerUp": pygame.image.load(BASE_DIR / "graphics" / "object" / "powerUp.png"),
    "explosion": pygame.image.load(BASE_DIR / "graphics" / "object" / "Explosion.png"),
}

FRAMES = {
    "list_icons": generate_icons_frames(),
    "list_cars": generate_frames(NUM_SKIN, CAR_WIDTH, CAR_HEIGHT),
    "explosion_animation": generate_frames(cant=12, width=150, height=150),
    "list_powerUp": generate_powerUp_frames(),
}

pygame.mixer.init()

SOUNDS = {
    "coin": pygame.mixer.Sound(BASE_DIR / "sounds" / "coin.wav"),
    "countdown": pygame.mixer.Sound(BASE_DIR / "sounds" / "countdown.wav"),
    "explosion": pygame.mixer.Sound(BASE_DIR / "sounds" / "explosion.wav"),
    "powerUp": pygame.mixer.Sound(BASE_DIR / "sounds" / "powerUp.wav"),
    "select": pygame.mixer.Sound(BASE_DIR / "sounds" / "menu_select.wav"),
    "select2": pygame.mixer.Sound(BASE_DIR / "sounds" / "menu_select2.wav"),
    "enter": pygame.mixer.Sound(BASE_DIR / "sounds" / "enter_button.wav"),
    "menu": pygame.mixer.Sound(BASE_DIR / "sounds" / "menu_stay_retro.ogg"),
    "play1": pygame.mixer.Sound(BASE_DIR / "sounds" / "play_fragment_of_tomorrow.ogg"),
    "play2": pygame.mixer.Sound(BASE_DIR / "sounds" / "play_hellfire.ogg"),
}

pygame.font.init()

FONTS = {
    "tiny": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 20),
    "small": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 32),
    "smallPlus": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 35),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 40),
    "mediumPlus": pygame.font.Font(
        BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 43
    ),
    "large": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 50),
    "largePlus": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 60),
    "timer": pygame.font.Font(BASE_DIR / "fonts" / "Supersonic Rocketship.ttf", 200),
}
