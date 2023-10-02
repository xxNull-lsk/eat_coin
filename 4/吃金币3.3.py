'''

炸弹来袭

'''
from pgzero_api_stub import *
import random
import pgzrun

STATUS_RUNNING = 1
STATUS_PAUSE = 2
STATUS_FINISH = 3

def update():
    '''控制主角移动'''
    global g_staus, g_score
    if g_staus != STATUS_RUNNING:
        return
    if keyboard.right:
        g_actor.x += 5
    elif keyboard.left:
        g_actor.x -= 5
    elif keyboard.up:
        g_actor.y -= 5
    elif keyboard.down:
        g_actor.y += 5

    g_actor.x = max(min(g_actor.x, WIDTH - g_actor.width), g_actor.width)
    g_actor.y = max(min(g_actor.y, HEIGHT - g_actor.height), g_actor.height)

def draw():
    '''绘制背景、角色和物品'''
    global g_score, g_staus, g_remain_time
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    if g_staus == STATUS_RUNNING:
        g_actor.draw()
        for stuff in g_stuffs:
            stuff.draw()
        screen.draw.text(f"剩余时间: {g_remain_time} 秒", (10, 10), fontname='default')
        screen.draw.text(f"现有分数: {g_score}", (10, 50), fontname='default')
    elif g_staus == STATUS_PAUSE:
        screen.draw.text(f"游戏已暂停", (500, 50), fontname='default')
    elif g_staus == STATUS_FINISH:
        screen.draw.text(f"游戏结束，得分: {g_score}", (500, 50), fontname='default')


def on_key_down(key):
    '''控制游戏状态'''
    global g_staus
    if key == keys.SPACE:
        if g_staus == STATUS_PAUSE:
            g_staus = STATUS_RUNNING
        elif g_staus == STATUS_RUNNING:
            g_staus = STATUS_PAUSE

def check_finish():
    '''计算游戏时间'''
    global g_remain_time, g_staus
    if g_remain_time > 0:
        g_remain_time -= 1
    else:
        g_staus = STATUS_FINISH

def is_valid_pos(s):
    '''防止道具重叠'''
    for stuff in g_stuffs:
        if s.colliderect(stuff):
            return False
    return True

def create_stuff():
    '''创建物品'''
    global g_stuffs
    count = 8 - len(g_stuffs)
    for i in range(count):
        if random.randint(3, 1000) % 5 == 1:
            stuff = Actor('bomb')
        else:
            stuff = Actor('coin')
        stuff.y = 0
        stuff.x = random.randint(stuff.width, WIDTH - stuff.width)
        while not is_valid_pos(stuff):
            stuff.x = random.randint(stuff.width, WIDTH - stuff.width)
        g_stuffs.append(stuff)


def check_stuff():
    '''计算物品'''
    global g_score, g_stuffs, g_remain_time, g_staus
    if g_staus != STATUS_RUNNING:
        return
    for i in range(len(g_stuffs)):
        stuff = g_stuffs[i]
        animate(stuff, pos=(stuff.x, stuff.y + 50))
        if stuff.y > HEIGHT:
            if stuff.image == 'coin':
                g_score -= 2
            del g_stuffs[i]
        elif stuff.colliderect(g_actor):
            if stuff.image == "coin":
                g_score += 1
            elif stuff.image == "bomb":
                g_remain_time -= 2
            del g_stuffs[i]
        create_stuff()

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 游戏分数
g_score = 0
# 剩余时间
g_remain_time = 30
# 游戏状态
g_staus = STATUS_RUNNING
# 物品集合
g_stuffs = []

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

# 加载物品
create_stuff()

# 定义时钟事件
clock.schedule_interval(check_finish, 1.0)
clock.schedule_interval(check_stuff, 0.1)

pgzrun.go()