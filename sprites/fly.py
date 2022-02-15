from sprites.enemy import Enemy
from sprites.player import Player


class Fly(Enemy):
    def define_y(self):
        return Player.GROUND_Y - 100

    def list_images_paths(self):
        return ['assets/graphics/fly/fly_1.png', 'assets/graphics/fly/fly_2.png']
