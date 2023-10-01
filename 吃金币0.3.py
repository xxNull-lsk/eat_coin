'''

新增主角移动控制

'''
import pgzrun

def update():
    pass

def draw():
    '''绘制背景、角色'''
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    g_actor.draw()

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

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

pgzrun.go()