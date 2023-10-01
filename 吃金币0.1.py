'''

新增背景

'''
import pgzrun

def update():
    pass

# 绘制背景
def draw():
    screen.clear()
    screen.blit('bg', pos=[0, 0])

# 设置窗口大小
WIDTH = 1024
HEIGHT = 512

pgzrun.go()