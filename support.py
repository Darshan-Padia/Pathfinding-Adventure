from csv import reader
from os import walk
import pygame
def import_csv_layout(path):
    terrain_map = []
    with open(path, 'r') as level_map:
        layout = reader(level_map,delimiter =',')
        for row in layout:
            # print(row)
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list=[]
    for _,__,img_files in walk(path):
        img_files.sort()
        for image in img_files:
            full_path = path +'/'+image
            # print("->_->- ",full_path)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    # surface_list.sort()
    return surface_list

# import_folder('graphics/grass')