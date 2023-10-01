'''

新增游戏时间

'''
import random
import pgzrun

def update():
    pass

def draw():
    '''绘制背景、角色和物品'''
    global g_score, g_remain_time
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    if g_remain_time <= 0:
        screen.draw.text(f"游戏结束，得分: {g_score}", (500, 50), fontname='default')
    else:
        g_actor.draw()
        g_stuff.draw()
        screen.draw.text(f"剩余时间: {g_remain_time} 秒", (10, 10), fontname='default')
        screen.draw.text(f"现有分数: {g_score}", (10, 50), fontname='default')

def on_key_down(key):
    '''控制角色移动'''
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

def check_finish():
    '''检查游戏剩余时间'''
    global g_remain_time
    if g_remain_time > 0:
        g_remain_time -= 1

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 游戏分数
g_score = 0
# 剩余时间
g_remain_time = 30

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

# 加载物品
g_stuff = Actor('coin')
g_stuff.x = random.randint(g_stuff.width, WIDTH - g_stuff.width)
g_stuff.y = random.randint(g_stuff.height, HEIGHT - g_stuff.height)

clock.schedule_interval(check_finish, 1.0)
pgzrun.go()