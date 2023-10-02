'''
新增物品支持
'''
from pgzero_api_stub import *
import random
import pgzrun

def update():
    pass

def draw():
    '''绘制背景、角色和物品'''
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    g_actor.draw()
    g_stuff.draw()

def on_key_down(key):
    '''控制角色移动'''
    if key == keys.RIGHT:
        g_actor.x += 10
    elif key == keys.LEFT:
        g_actor.x -= 10
    elif key == keys.UP:
        g_actor.y -= 10
    elif key == keys.DOWN:
        g_actor.y += 10
    
    if g_actor.colliderect(g_stuff):
        g_stuff.x = random.randint(0, WIDTH)
        g_stuff.y = random.randint(0, HEIGHT)

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

# 加载物品
g_stuff = Actor('coin')
g_stuff.x = random.randint(0, WIDTH)
g_stuff.y = random.randint(0, HEIGHT)

pgzrun.go()