from sprites.enemy import Enemy
from sprites.player import Player


class Snail(Enemy):
    def define_y(self):
        return Player.GROUND_Y

    def list_images_paths(self):
        return ['assets/graphics/snail/snail_1.png', 'assets/graphics/snail/snail_2.png']
