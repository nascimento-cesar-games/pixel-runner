import pygame


class Player(pygame.sprite.Sprite):
    GROUND_Y = 300
    JUMP_GRAVITY = -20
    IMAGE_JUMP_PATH = 'assets/graphics/player/jump.png'
    IMAGE_WALK_1_PATH = 'assets/graphics/player/player_walk_1.png'
    IMAGE_WALK_2_PATH = 'assets/graphics/player/player_walk_2.png'
    SOUND_JUMP_PATH = 'assets/audio/jump.mp3'

    def __init__(self):
        super().__init__()

        self.image_walk_index = 0
        self.image_walk_1 = pygame.image.load(
            Player.IMAGE_WALK_1_PATH).convert_alpha()
        self.image_walk_2 = pygame.image.load(
            Player.IMAGE_WALK_2_PATH).convert_alpha()
        self.image_jump = pygame.image.load(
            Player.IMAGE_JUMP_PATH).convert_alpha()

        self.image = self.define_current_image()
        self.rect = self.image.get_rect(midbottom=(80, Player.GROUND_Y))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound(Player.SOUND_JUMP_PATH)
        self.jump_sound.set_volume(0.1)

    def define_current_image(self):
        image_walk_list = [self.image_walk_1, self.image_walk_2]
        return image_walk_list[int(self.image_walk_index)]

    def has_landed_ground(self):
        return self.rect.bottom >= Player.GROUND_Y

    def handle_input(self):
        keys = pygame.key.get_pressed()

        is_space_pressed = keys[pygame.K_SPACE]

        if is_space_pressed and self.has_landed_ground():
            self.gravity = Player.JUMP_GRAVITY
            self.jump_sound.play()

    def apply_animation(self):
        if not self.has_landed_ground():
            self.image = self.image_jump
        else:
            self.image_walk_index += 0.1
            image_walk_count = 2

            if self.image_walk_index >= image_walk_count:
                self.image_walk_index = 0

            self.image = self.define_current_image()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.has_landed_ground():
            self.rect.bottom = Player.GROUND_Y

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.apply_animation()
