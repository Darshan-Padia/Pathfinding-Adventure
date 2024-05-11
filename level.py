from tkinter import Toplevel
import pygame as pg
from settings import *
from tile import Tile
from player import Player
from debug import *
from support import *
from random import choice
from TH_terminal import *
# from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self):
        # get the display surface
        # self.tmx_data = load_pygame('/home/darshan/college/tiled2_fin/tmx/th.tmx')
        self.display_surface = pg.display.get_surface()
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()

        # sprite setup
        self.create_map()


    

    # setting up the world
    def create_map(self):
        layouts = {
            'boundary':import_csv_layout('thunt_floor_blocks.csv'),
            # 'grass':import_csv_layout('map/map_Grass.csv'),
            'object':import_csv_layout('thunt_Objects_trees_rocks.csv')

        }
        graphics ={
            'grass':import_folder('graphics/grass'),
            'objects':import_folder('graphics/objects')
        }
        lst = []
        # print(graphics['objects'])
        for style,layout in layouts.items():
            for row_index , row in enumerate(layout):# y position( not a mistake)
                for col_index , col in enumerate(row): # for x position
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        lst.append((x,y))

                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        # grass
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        # object
                        if style == 'object':

                            # if(int(col) >= 0  and int(col) <=10):
                            try:
                                surf = graphics['objects'][int(col)]
                            except:
                                print(int(col))
                            # print(surf)
                            # random_object_image = choice(graphics['objects'])
                            # print(self.tmx_data.get_object_by_id(int(col)))
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                            if(int(col) == 14):
                                print(f'({x},{y}),')
                    



        k,l = 2000,1500
        for i in DIALOG_OBJECT.keys():
            if DIALOG_OBJECT[i] == str(start_node):
                k,l = i
                break
        if start_node == 6709:
            l-=2*64
        else:
            k+=64


        self.player = Player((k,l), [self.visible_sprites] , self.obstacle_sprites  )
                
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.status) 
        debug(self.player.score)
        
        
                    
                
class YSortCameraGroup(pg.sprite.Group):
    def __init__(self ):
        # general setup
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

        # creating the floor
        self.floor_surf = pg.image.load('graphics/tilemap/th.png').convert()
        self.floor_rect= self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites() , key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        
    