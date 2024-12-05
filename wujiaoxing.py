import turtle

# 创建一个新的turtle对象
t = turtle.Turtle()

# 将画笔设置为不留痕
t.penup()
t.goto(-150, 100)
t.pendown()

# 开始绘制五角星
def draw_star(t, size):
    angle = 144
    for i in range(5):
        t.forward(size)
        t.right(angle)

# 绘制一个大小为200的五角星
draw_star(t, 200)

# 等待用户关闭窗口
turtle.done()