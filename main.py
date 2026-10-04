import pygame
import random
from Cat import Cat
from Vector import Vector
from Animation import Animation
from Block import Block
from Hitbox import Hitbox

pygame.init()
SCREEN_X = 1000
SCREEN_Y = 800
screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))

def define_hitbox(position, width=None, height=None, image=None):
    width = width or image.get_width()
    height = height or image.get_height()
    return Hitbox(screen, position, width, height)

floor_position = Vector(0,0)
floor_hitbox = define_hitbox(floor_position, SCREEN_X, SCREEN_Y/16)
floor = Block(None, floor_position, 0, floor_hitbox)

catwalkleft1 = pygame.image.load(r"C:\Users\janso\easy_access_files\platformer\assets\walk-left-1.png").convert_alpha()
catwalkleft2 = pygame.image.load(r"C:\Users\janso\easy_access_files\platformer\assets\walk-left-2.png").convert_alpha()
catwalkleft1 = pygame.transform.scale_by(catwalkleft1, 4)
catwalkleft2 = pygame.transform.scale_by(catwalkleft2, 4)

cat_animation = Animation(screen, [catwalkleft1, catwalkleft2])
cat_position = Vector(200, 700)
cat_velocity = Vector(0,0)
cat_hitbox = define_hitbox(cat_position, image=catwalkleft1)
cat = Cat(cat_animation, cat_position, cat_velocity, cat_hitbox)

block_list = [
    r"C:\Users\janso\easy_access_files\platformer\assets\flat-block.png",
    r"C:\Users\janso\easy_access_files\platformer\assets\donut-block.png",
    r"C:\Users\janso\easy_access_files\platformer\assets\sideways-donut-block.png"
]

blocks = []
BLOCKS = 7
for i in range(BLOCKS):
    flat_block = pygame.image.load(block_list[random.randint(0,2)]).convert_alpha()
    block_img = pygame.transform.scale_by(flat_block, 4)
    block_animation = Animation(screen, [block_img])
    block_position = Vector(200 + i*100, i*100 + 200)
    block_velocity = Vector(0,0.1)
    block_hitbox = define_hitbox(block_position, image=block_img)
    blocks.append(Block(block_animation, block_position, block_velocity, block_hitbox))

def manage_positions():
    cat.stayStill()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cat.goLeft()
    if keys[pygame.K_RIGHT]:
        cat.goRight()
    if keys[pygame.K_UP]:
        cat.goUp()
    if keys[pygame.K_DOWN]:
        cat.goDown()
    if keys[pygame.K_SPACE]:
        cat.jump()
    cat.move()
    for block in blocks:
        block.move()

def manage_collisions():
    for block in blocks:
        if cat.hitbox.isColliding(block.hitbox):
            pass

    if cat.hitbox.isColliding(floor.hitbox):
        pass

running = True
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    manage_positions()

    screen.fill((225, 169, 246))
    for block in blocks:
        block.draw()
    cat.draw()
    cat.hitbox.draw()
    floor.hitbox.draw()
    pygame.display.update() 

pygame.quit()