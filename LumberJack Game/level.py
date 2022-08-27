import pygame
from setting import *
from tile import Tile
from player import Player

#Class for organize the core functions of the game
class Level:
    def __init__(self,level_data,surface):
        #level set up
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    
    #Method for draw the level layout (level_data)
    def setup_level(self,layout): 
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                x = col_index*tile_size
                y = row_index*tile_size
                if col == 'X':
                   tile = Tile((x,y),tile_size)
                   self.tiles.add(tile)
                elif col == 'P':
                   player_sprite = Player((x,y))
                   self.player.add(player_sprite)
            
    #Method for run the game    
    def run(self):
         self.tiles.update(self.world_shift)
         self.tiles.draw(self.display_surface)
         
         self.player.update()
         self.player.draw(self.display_surface)
         
        

