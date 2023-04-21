
import pygame 

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputData
from gale.text import render_text

import settings
from src.Player import Player

class CarSelectState(BaseState):
    def enter(self) -> None:
        self.player = Player((settings.VIRTUAL_WIDTH - settings.TEXTURES["car1"].get_width()) // 2 , (settings.VIRTUAL_HEIGHT - settings.TEXTURES["car1"].get_height()) // 2)
        self.select = 0
        self.retardo = False
        self.displayX = 0.0
        InputHandler.register_listener(self)
  
    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        self.retardo = True
        if self.displayX < settings.VIRTUAL_WIDTH * 2:
            self.displayX += (settings.VIRTUAL_WIDTH // 10.0) * 2

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_right" and input_data.pressed:           
            self.player.skin = min(7, self.player.skin + 1)
        elif input_id == "move_left" and input_data.pressed:
            self.player.skin = max(0, self.player.skin - 1)
        elif input_id == "enter" and input_data.pressed and self.retardo:
            self.state_machine.change("play", player=self.player)

    def render(self, surface: pygame.Surface) -> None:    
        if self.displayX < settings.VIRTUAL_WIDTH:
            surface.blit(settings.TEXTURES["EscenaStar"], [self.displayX,0])
        elif self.displayX < settings.VIRTUAL_WIDTH * 2:
            surface.blit(settings.TEXTURES["EscenaSelect"], (self.displayX - settings.VIRTUAL_WIDTH *2, 0))
        else:    
            surface.blit(settings.TEXTURES["EscenaSelect"], (0, 0))
            surface.blit(settings.TEXTURES["cartel1"], ((settings.VIRTUAL_WIDTH - settings.TEXTURES["cartel1"].get_width()) // 2, (settings.VIRTUAL_HEIGHT - settings.TEXTURES["cartel1"].get_height()) // 2))
            
            render_text(
            surface,
            "Select your car",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            110,
            (0, 0, 0),
            center= True,
            )
            self.player.render(surface)
        