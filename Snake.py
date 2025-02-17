import pygame
import random

import Player

pygame.init

width = 700
height = 700

screen = pygame.display.set_mode((width, height))

grid_cell_size = 10
grid_size = 70
grid_size_px = grid_size * grid_cell_size

player = Player.Player(grid_cell_size)

player_sprite = pygame.Rect(
            (player.position['x'], player.position['y']), 
            (grid_cell_size, grid_cell_size)
        )

wall_w = pygame.Rect(
            (0, 0), 
            (grid_cell_size, grid_size_px)
        )
wall_e = pygame.Rect(
            (grid_size_px - grid_cell_size, 0), 
            (grid_cell_size, grid_size_px)
        )
wall_n = pygame.Rect(
            (0, 0), 
            (grid_size_px, grid_cell_size)
        )
wall_s = pygame.Rect(
            (0, grid_size_px - grid_cell_size), 
            (grid_size_px, grid_cell_size)
        )


player_move_delay_ms = 500

pygame.display.set_caption('Snake Game')

pygame.time.set_timer(0, player_move_delay_ms)

def randomize_player_start():
    player.position['x'] = grid_cell_size * random.randrange(3, grid_size - 3)
    player.position['y'] = grid_cell_size * random.randrange(3, grid_size - 3)

def draw_walls(screen, wall_w, wall_e, wall_n, wall_s):
    pygame.draw.rect(
        screen, 
        (255, 0, 0), 
        wall_n
    )
    pygame.draw.rect(
        screen, 
        (255, 0, 0), 
        wall_s
    )
    pygame.draw.rect(
        screen, 
        (255, 0, 0), 
        wall_e
    )
    pygame.draw.rect(
        screen, 
        (255, 0, 0), 
        wall_w
    )

randomize_player_start()


death_objects = {
    tuple(wall_e): 0, 
    tuple(wall_n): 1, 
    tuple(wall_s): 2, 
    tuple(wall_w): 3
}

segment_sprites = []

def add_segment_sprite(x, y):
    segment_sprites.append(pygame.Rect(
            (x, y), 
            (grid_cell_size, grid_cell_size)
        ))

def move_fruit():
    x = random.randrange(grid_cell_size, grid_size_px - grid_cell_size, grid_cell_size)
    y = random.randrange(grid_cell_size, grid_size_px - grid_cell_size, grid_cell_size)
    return pygame.Rect(
        (x,y),
        (grid_cell_size, grid_cell_size)
    )

fruit = move_fruit()

running = True
while running:
    screen.fill((0,0,0))
    draw_walls(screen, wall_w, wall_e, wall_n, wall_s)
    player_sprite = pygame.Rect(
            (player.position['x'], player.position['y']), 
            (grid_cell_size, grid_cell_size)
        )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.change_direction(event.dict['key'])
        if event.type == 0:
            player.move()
            segment_sprites.clear()
            for seg in player.segments:
                add_segment_sprite(seg['x'], seg['y'])
            if player.self_destruct:
                running = False
                

            if(player_sprite.collidedict(death_objects)):
                running = False

    if(player_sprite.colliderect(fruit)):
        fruit = move_fruit()
        player.add_segment(-1,-1)
        player_move_delay_ms = player_move_delay_ms - 10
        player_move_delay_ms = min(max(1, player_move_delay_ms), 500)
        pygame.time.set_timer(0, player_move_delay_ms)

    pygame.draw.rect(
        screen, 
        (255, 255, 255), 
        player_sprite
    )

    pygame.draw.rect(
        screen,
        (0,255,0),
        fruit
    )

    for seg in segment_sprites:
        pygame.draw.rect(
        screen, 
        (255, 255, 255), 
        seg
    )

    pygame.display.flip()

pygame.quit()



