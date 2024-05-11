from pytmx.util_pygame import load_pygame

import pygame, sys

# from pytmx.util_pygame import load_pygame

# tmx_data = 
class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode ( (400, 600) )
        pygame.display.set_caption("Treasure Hunt") 
        self.clock = pygame.time.Clock()
        # global data_tmx
        self.data_tmx = load_pygame("/home/darshan/college/tiled2_fin/tmx/th.tmx")
        
        # self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame .quit()
                    sys.exit()
            self.screen.fill('black')
            # self.level.run()
            # debug("hello:)")
            pygame.display.update()
            self.clock.tick(60)
    def any(self):
        self.tmx_data = load_pygame('/home/darshan/college/tiled2_fin/tmx/th.tmx')
        tile_layer = self.tmx_data.get_layer_by_name('Objects_trees_rocks')
        # for i in range(12,100):
        print(self.tmx_data.objects_by_id)
            # print(tile_object)

        #     print(tile)
if __name__ == '__main__':
    game = Game()
    game.any()
    game.run()
