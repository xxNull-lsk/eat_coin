'''

新增游戏分数

'''
import random
import pgzrun

def update():
    pass

# 绘制背景、角色和物品
def draw():
    global g_score
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    g_actor.draw()
    g_stuff.draw()
    screen.draw.text(f"现有分数: {g_score}", (10, 10), fontname='default')

# 控制角色移动
def on_key_down(key):
    global g_score, g_remain_time
    if g_remain_time <= 0:
        return
    if key == keys.RIGHT:
        g_actor.x += 10
    elif key == keys.LEFT:
        g_actor.x -= 10
    elif key == keys.UP:
        g_actor.y -= 10
    elif key == keys.DOWN:
        g_actor.y += 10

    g_actor.x = max(min(g_actor.x, WIDTH - g_actor.width), g_actor.width)
    g_actor.y = max(min(g_actor.y, HEIGHT - g_actor.height), g_actor.height)
    
    if g_actor.colliderect(g_stuff):
        g_score += 1
        g_stuff.x = random.randint(g_stuff.width, WIDTH - g_stuff.width)
        g_stuff.y = random.randint(g_stuff.height, HEIGHT - g_stuff.height)

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 游戏分数
g_score = 0

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

# 加载物品
g_stuff = Actor('coin')
g_stuff.x = random.randint(g_stuff.width, WIDTH - g_stuff.width)
g_stuff.y = random.randint(g_stuff.height, HEIGHT - g_stuff.height)

pgzrun.go()
