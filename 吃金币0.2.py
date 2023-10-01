'''

新增主角

'''
import pgzrun

def update():
    pass

# 绘制背景、主角
def draw():
    screen.clear()
    screen.blit('bg', pos=[0, 0])
    g_actor.draw()

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

# 加载主角
g_actor = Actor("alien")
g_actor.x = 250
g_actor.y = 250

pgzrun.go()
