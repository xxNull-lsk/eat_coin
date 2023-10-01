'''

新增边界检查

'''
import random
import pgzrun

def update():
    pass

# 绘制背景、角色和物品
def draw():
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    g_actor.draw()
    g_stuff.draw()

# 控制角色移动
def on_key_down(key):
    if key == keys.RIGHT:
        g_actor.x += 10
    elif key == keys.LEFT:
        g_actor.x -= 10
    elif key == keys.UP:
        g_actor.y -= 10
    elif key == keys.DOWN:
        g_actor.y += 10

    if g_actor.x > WIDTH - g_actor.width:
        g_actor.x = WIDTH - g_actor.width
    elif g_actor.x < g_actor.width:
        g_actor.x = g_actor.width

    if g_actor.y > HEIGHT - g_actor.height:
        g_actor.y = HEIGHT - g_actor.height
    elif g_actor.y < g_actor.height:
        g_actor.y = g_actor.height
    
    if g_actor.colliderect(g_stuff):
        g_stuff.x = random.randint(g_stuff.width, WIDTH - g_stuff.width)
        g_stuff.y = random.randint(g_stuff.height, HEIGHT - g_stuff.height)

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

# 加载物品
g_stuff = Actor('coin')
g_stuff.x = random.randint(g_stuff.width, WIDTH - g_stuff.width)
g_stuff.y = random.randint(g_stuff.height, HEIGHT - g_stuff.height)

pgzrun.go()
