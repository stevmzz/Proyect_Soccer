import pygame
from pygame.locals import *

##########################################################################################################

pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), FULLSCREEN)
pygame.display.set_caption("BOMBERMAN by steven")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('sounds/𝗱𝗼𝗿𝗶𝗮𝗻 𝗰𝗼𝗻𝗰𝗲𝗽𝘁 - 𝗵𝗶𝗱𝗲 (𝗰𝘀𝟬𝟭) (𝗺𝘆𝘀𝘁𝗲𝗿𝗶𝗼𝘂𝘀 𝗱𝘂𝗻𝗴𝗲𝗼𝗻_𝘀𝗹𝗼𝘄𝗲𝗱 + 𝗿𝗲𝘃𝗲𝗿𝗯).mp3')
pygame.mixer.music.play(-1)

##########################################################################################################

back_img = pygame.transform.scale(pygame.image.load("images/skin1/atras.png").convert_alpha(), (45, 45))
front_img = pygame.transform.scale(pygame.image.load("images/skin1/frente.png").convert_alpha(), (45, 45))
right_img = pygame.transform.scale(pygame.image.load("images/skin1/der.png").convert_alpha(), (45, 45))
left_img = pygame.transform.scale(pygame.image.load("images/skin1/izq.png").convert_alpha(), (45, 45))

player_img = front_img
player_rect = player_img.get_rect()
player_rect.center = (130, 110)

##########################################################################################################

player_rect_old_x, player_rect_old_y = player_rect.x, player_rect.y

##########################################################################################################

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

##########################################################################################################

wall_img = pygame.transform.scale(pygame.image.load("images/textures/piedradura.png").convert_alpha(), (55, 55))
wall_width, wall_height = wall_img.get_size()

green_area_width = 1265
green_area_height = 713
green_area_x = (info.current_w - green_area_width) // 2
green_area_y = (info.current_h - green_area_height) // 2

speed = 4

##########################################################################################################

enemy_img = pygame.transform.scale(pygame.image.load("images/enemigo1.png").convert_alpha(), (45, 45))

enemy1_rect = enemy_img.get_rect(center=(green_area_x + 200, green_area_y + 80))
enemy2_rect = enemy_img.get_rect(center=(green_area_x + 500, green_area_y + 300))
enemy6_rect = enemy_img.get_rect(center=(green_area_x + 800, green_area_y + 410))
enemy3_rect = enemy_img.get_rect(center=(green_area_x + 1000, green_area_y + 630))

enemy4_rect = enemy_img.get_rect(center=(green_area_x + 190, green_area_y + 120))
enemy5_rect = enemy_img.get_rect(center=(green_area_x + 410, green_area_y + 560))
enemy7_rect = enemy_img.get_rect(center=(green_area_x + 630, green_area_y + 220))
enemy8_rect = enemy_img.get_rect(center=(green_area_x + 850, green_area_y + 660))
enemy9_rect = enemy_img.get_rect(center=(green_area_x + 1070, green_area_y + 320))

enemy4_speed = 3
enemy5_speed = 3
enemy7_speed = 3
enemy8_speed = 3
enemy9_speed = 3

enemy1_speed = 3  
enemy2_speed = 5 
enemy3_speed = 5 
enemy6_speed = 3 

##########################################################################################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[K_w] or keys[K_UP]:
        player_rect.y -= speed if player_rect.top > green_area_y else 0
        player_img = back_img
    if keys[K_s] or keys[K_DOWN]:
        player_rect.y += speed if player_rect.bottom < green_area_y + green_area_height else 0
        player_img = front_img
    if keys[K_a] or keys[K_LEFT]:
        player_rect.x -= speed if player_rect.left > green_area_x else 0
        player_img = left_img
    if keys[K_d] or keys[K_RIGHT]:
        player_rect.x += speed if player_rect.right < green_area_x + green_area_width else 0
        player_img = right_img

##########################################################################################################

    enemy1_rect.x += enemy1_speed

    if enemy1_speed < 0 and maze[(enemy1_rect.centery - green_area_y) // wall_height][(enemy1_rect.left - green_area_x) // wall_width] == 1:
        enemy1_speed *= -1 
        enemy1_rect.left = green_area_x + (enemy1_rect.left - green_area_x) // wall_width * wall_width + wall_width

    elif enemy1_speed > 0 and maze[(enemy1_rect.centery - green_area_y) // wall_height][(enemy1_rect.right - 1 - green_area_x) // wall_width] == 1:
        enemy1_speed *= -1
        enemy1_rect.right = green_area_x + (enemy1_rect.right - green_area_x) // wall_width * wall_width

##########################################################################################################

    enemy2_rect.x += enemy2_speed

    if enemy2_speed < 0 and maze[(enemy2_rect.centery - green_area_y) // wall_height][(enemy2_rect.left - green_area_x) // wall_width] == 1:
        enemy2_speed *= -1
        enemy2_rect.left = green_area_x + (enemy2_rect.left - green_area_x) // wall_width * wall_width + wall_width

    elif enemy2_speed > 0 and maze[(enemy2_rect.centery - green_area_y) // wall_height][(enemy2_rect.right - 1 - green_area_x) // wall_width] == 1:
        enemy2_speed *= -1
        enemy2_rect.right = green_area_x + (enemy2_rect.right - green_area_x) // wall_width * wall_width

##########################################################################################################

    enemy3_rect.x += enemy3_speed

    if enemy3_speed < 0 and maze[(enemy3_rect.centery - green_area_y) // wall_height][(enemy3_rect.left - green_area_x) // wall_width] == 1:
        enemy3_speed *= -1  
        enemy3_rect.left = green_area_x + (enemy3_rect.left - green_area_x) // wall_width * wall_width + wall_width

    elif enemy3_speed > 0 and maze[(enemy3_rect.centery - green_area_y) // wall_height][(enemy3_rect.right - 1 - green_area_x) // wall_width] == 1:
        enemy3_speed *= -1  
        enemy3_rect.right = green_area_x + (enemy3_rect.right - green_area_x) // wall_width * wall_width

##########################################################################################################

    enemy6_rect.x += enemy6_speed

    if enemy6_speed < 0 and maze[(enemy6_rect.centery - green_area_y) // wall_height][(enemy6_rect.left - green_area_x) // wall_width] == 1:
        enemy6_speed *= -1  
        enemy6_rect.left = green_area_x + (enemy6_rect.left - green_area_x) // wall_width * wall_width + wall_width

    elif enemy6_speed > 0 and maze[(enemy6_rect.centery - green_area_y) // wall_height][(enemy6_rect.right - 1 - green_area_x) // wall_width] == 1:
        enemy6_speed *= -1  
        enemy6_rect.right = green_area_x + (enemy6_rect.right - green_area_x) // wall_width * wall_width

##########################################################################################################

    enemy4_rect.y += enemy4_speed

    if enemy4_speed < 0 and maze[(enemy4_rect.top - green_area_y) // wall_height][(enemy4_rect.centerx - green_area_x) // wall_width] == 1:
        enemy4_speed *= -1  
        enemy4_rect.top = green_area_y + (enemy4_rect.top - green_area_y) // wall_height * wall_height + wall_height

    elif enemy4_speed > 0 and maze[(enemy4_rect.bottom - 1 - green_area_y) // wall_height][(enemy4_rect.centerx - green_area_x) // wall_width] == 1:
        enemy4_speed *= -1 
        enemy4_rect.bottom = green_area_y + (enemy4_rect.bottom - green_area_y) // wall_height * wall_height

##########################################################################################################

    enemy5_rect.y += enemy5_speed

    if enemy5_speed < 0 and maze[(enemy5_rect.top - green_area_y) // wall_height][(enemy5_rect.centerx - green_area_x) // wall_width] == 1:
        enemy5_speed *= -1  
        enemy5_rect.top = green_area_y + (enemy5_rect.top - green_area_y) // wall_height * wall_height + wall_height

    elif enemy5_speed > 0 and maze[(enemy5_rect.bottom - 1 - green_area_y) // wall_height][(enemy5_rect.centerx - green_area_x) // wall_width] == 1:
        enemy5_speed *= -1 
        enemy5_rect.bottom = green_area_y + (enemy5_rect.bottom - green_area_y) // wall_height * wall_height

##########################################################################################################

    enemy7_rect.y += enemy7_speed

    if enemy7_speed < 0 and maze[(enemy7_rect.top - green_area_y) // wall_height][(enemy7_rect.centerx - green_area_x) // wall_width] == 1:
        enemy7_speed *= -1  
        enemy7_rect.top = green_area_y + (enemy7_rect.top - green_area_y) // wall_height * wall_height + wall_height

    elif enemy7_speed > 0 and maze[(enemy7_rect.bottom - 1 - green_area_y) // wall_height][(enemy7_rect.centerx - green_area_x) // wall_width] == 1:
        enemy7_speed *= -1  
        enemy7_rect.bottom = green_area_y + (enemy7_rect.bottom - green_area_y) // wall_height * wall_height

##########################################################################################################

    enemy8_rect.y += enemy8_speed

    if enemy8_speed < 0 and maze[(enemy8_rect.top - green_area_y) // wall_height][(enemy8_rect.centerx - green_area_x) // wall_width] == 1:
        enemy8_speed *= -1  
        enemy8_rect.top = green_area_y + (enemy8_rect.top - green_area_y) // wall_height * wall_height + wall_height

    elif enemy8_speed > 0 and maze[(enemy8_rect.bottom - 1 - green_area_y) // wall_height][(enemy8_rect.centerx - green_area_x) // wall_width] == 1:
        enemy8_speed *= -1 
        enemy8_rect.bottom = green_area_y + (enemy8_rect.bottom - green_area_y) // wall_height * wall_height

##########################################################################################################

    enemy9_rect.y += enemy9_speed

    if enemy9_speed < 0 and maze[(enemy9_rect.top - green_area_y) // wall_height][(enemy9_rect.centerx - green_area_x) // wall_width] == 1:
        enemy9_speed *= -1  
        enemy9_rect.top = green_area_y + (enemy9_rect.top - green_area_y) // wall_height * wall_height + wall_height

    elif enemy9_speed > 0 and maze[(enemy9_rect.bottom - 1 - green_area_y) // wall_height][(enemy9_rect.centerx - green_area_x) // wall_width] == 1:
        enemy9_speed *= -1  
        enemy9_rect.bottom = green_area_y + (enemy9_rect.bottom - green_area_y) // wall_height * wall_height

##########################################################################################################

    if player_rect.colliderect(enemy1_rect) or player_rect.colliderect(enemy2_rect) or player_rect.colliderect(enemy3_rect) or player_rect.colliderect(enemy4_rect) or player_rect.colliderect(enemy5_rect) or player_rect.colliderect(enemy6_rect) or player_rect.colliderect(enemy7_rect) or player_rect.colliderect(enemy8_rect) or player_rect.colliderect(enemy9_rect):
        running = False

##########################################################################################################

    for row_index, row in enumerate(maze):
        for col_index, block in enumerate(row):
            if block == 1:
                wall_rect = wall_img.get_rect(topleft=(green_area_x + col_index * wall_width,
                                                        green_area_y + row_index * wall_height))
                if player_rect.colliderect(wall_rect):
                    player_rect.x = player_rect.x - (player_rect.x - player_rect_old_x)
                    player_rect.y = player_rect.y - (player_rect.y - player_rect_old_y)

    player_rect_old_x, player_rect_old_y = player_rect.x, player_rect.y

##########################################################################################################

    player_rect.x = max(green_area_x, min(player_rect.x, green_area_x + green_area_width - player_rect.width))
    player_rect.y = max(green_area_y, min(player_rect.y, green_area_y + green_area_height - player_rect.height))

    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen, (144, 238, 144), (green_area_x, green_area_y, green_area_width, green_area_height))  

    stone_img = pygame.transform.scale(pygame.image.load("images/textures/cesped1.png").convert_alpha(), (wall_width, wall_height))

##########################################################################################################

    for row_index, row in enumerate(maze):
        for col_index, block in enumerate(row):
            if block == 1:
                wall_rect = wall_img.get_rect(topleft=(green_area_x + col_index * wall_width,
                                                        green_area_y + row_index * wall_height))
                screen.blit(wall_img, wall_rect)
            elif block == 0:
                stone_rect = wall_img.get_rect(topleft=(green_area_x + col_index * wall_width,
                                                         green_area_y + row_index * wall_height))
                screen.blit(stone_img, stone_rect)

##########################################################################################################

    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy1_rect)
    screen.blit(enemy_img, enemy2_rect)
    screen.blit(enemy_img, enemy3_rect)
    screen.blit(enemy_img, enemy4_rect)
    screen.blit(enemy_img, enemy5_rect)
    screen.blit(enemy_img, enemy6_rect)
    screen.blit(enemy_img, enemy7_rect)
    screen.blit(enemy_img, enemy8_rect)
    screen.blit(enemy_img, enemy9_rect)

    pygame.display.flip()

pygame.quit()
