
import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings
from src.Player import Player


class PlayState(BaseState):
    def enter(self, **params: dict) -> None:  
        self.posX = 610
        self.posY = settings.VIRTUAL_HEIGHT - 230 
        self.wallLeft = 460
        self.wallRight = 1000
        self.player = params["player"]
        self.player.x = self.posX
        self.player.y = self.posY 
        self.displayX = 0
        self.displayY = 0
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.yRelativa = self.displayY % settings.VIRTUAL_HEIGHT
        self.displayY += 50  

        self.player.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["Soil_Tile"],[self.displayX, self.yRelativa - settings.VIRTUAL_HEIGHT])        
        surface.blit(settings.TEXTURES["road_0_left"],[380, self.yRelativa - settings.VIRTUAL_HEIGHT])
        surface.blit(settings.TEXTURES["road_0_right"],[730, self.yRelativa - settings.VIRTUAL_HEIGHT])
        if self.yRelativa < settings.VIRTUAL_HEIGHT:
            surface.blit(settings.TEXTURES["Soil_Tile"],[self.displayX, self.yRelativa])
            surface.blit(settings.TEXTURES["road_0_left"],[380, self.yRelativa])
            surface.blit(settings.TEXTURES["road_0_right"],[730, self.yRelativa])
        self.player.render(surface)
        pygame.display.flip()
        
    
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.player.vx = -settings.PLAYER_SPEED
            elif input_data.released and self.player.vx < 0:
                self.player.vx = 0
        elif input_id == "move_right":
            if input_data.pressed:
                self.player.vx = settings.PLAYER_SPEED
            elif input_data.released and self.player.vx > 0:
                self.player.vx = 0
        elif input_id == "move_up":
            if input_data.pressed:
                self.player.vy = -settings.PLAYER_SPEED
            elif input_data.released and self.player.vy < 0:
                self.player.vy = 0
        elif input_id == "move_down":
            if input_data.pressed:
                self.player.vy = settings.PLAYER_SPEED
            elif input_data.released and self.player.vy > 0:
                self.player.vy = 0

        
        
        
        
        