from vpython import *


# 초기화
ball = sphere(radius=0.2)

ball.pos = vec(-2, 0, 0)
ball.v = vec(0.8, 0.1, 0)

t = 0
dt = 0.01

# 속도 벡터
attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)


# 시뮬레이션
while t < 5:
	rate(1 / dt)
	ball.pos = ball.pos + ball.v * dt
	t = t + dt
