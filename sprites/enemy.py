from random import randint
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animation_image_index = 0
        self.image = self.define_current_image()
        self.rect = self.image.get_rect(
            midbottom=(randint(900, 1100), self.define_y()))

    def define_y(self):
        raise NotImplementedError

    def define_current_image(self):
        animation_image_list = list(
            map(self.build_image, self.list_images_paths()))
        return animation_image_list[int(self.animation_image_index)]

    def build_image(self, image_path):
        return pygame.image.load(image_path).convert_alpha()

    def list_images_paths(self):
        raise NotImplementedError

    def apply_animation(self):
        self.animation_image_index += 0.1
        animation_image_count = 2

        if self.animation_image_index >= animation_image_count:
            self.animation_image_index = 0

        self.image = self.define_current_image()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.apply_animation()
        self.rect.x -= 6
        self.destroy()
