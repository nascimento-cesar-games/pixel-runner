from random import choice, randint
from sprites.fly import Fly
from sprites.player import Player
from sprites.snail import Snail
import pygame


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surface = game_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time


def setup_screen():
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("My first pygame")
    return screen


def has_collision():
    collided_sprite = pygame.sprite.spritecollide(
        player_group.sprite, enemy_group, False)

    if collided_sprite:
        enemy_group.empty()
        return True
    else:
        return False


def setup_sky_surface():
    return pygame.image.load('assets/graphics/sky.png').convert()


def setup_ground_surface():
    return pygame.image.load('assets/graphics/ground.png').convert()


pygame.init()

screen = setup_screen()
clock = pygame.time.Clock()
is_game_active = False
start_time = 0
score = 0

player_group = pygame.sprite.GroupSingle()
player_group.add(Player())

enemy_group = pygame.sprite.Group()

game_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

background_music = pygame.mixer.Sound('assets/audio/music.wav')
background_music.set_volume(0.1)
background_music.play(loops=-1)

sky_surface = setup_sky_surface()

ground_surface = setup_ground_surface()
ground_x = 0
ground_y = 300

game_title_surface = game_font.render('Pixel Runner', False, (111, 196, 169))
game_title_rectangle = game_title_surface.get_rect(center=(400, 80))

game_instructions_surface = game_font.render(
    'Press space to run', False, (111, 196, 169))
game_instructions_rectangle = game_instructions_surface.get_rect(
    center=(400, 320))

start_screen_image = pygame.image.load(
    'assets/graphics/player/player_stand.png').convert_alpha()
start_screen_surface = pygame.transform.scale2x(start_screen_image)
start_screen_rectangle = start_screen_surface.get_rect(
    center=(400, 200))

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

obstacle_rectangle_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if is_game_active:
            if event.type == enemy_timer:
                enemy_group.add(choice([Snail(), Snail(), Snail(), Fly()]))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_game_active = True
                start_time = pygame.time.get_ticks()

    if is_game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (ground_x, ground_y))

        score = display_score()

        player_group.draw(screen)
        player_group.update()

        enemy_group.draw(screen)
        enemy_group.update()

        is_game_active = not has_collision()
    else:
        screen.fill((94, 129, 162))
        screen.blit(start_screen_surface, start_screen_rectangle)
        screen.blit(game_title_surface, game_title_rectangle)

        if score == 0:
            screen.blit(game_instructions_surface, game_instructions_rectangle)
        else:
            final_score_surface = game_font.render(
                f'Your score: {score}', False, (111, 196, 169))
            final_score_rectangle = final_score_surface.get_rect(
                center=(400, 320))
            screen.blit(final_score_surface, final_score_rectangle)

    pygame.display.update()
    clock.tick(60)
