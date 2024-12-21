from vpython import *


# 초기화
ball = sphere(radius=0.2)

ball.pos = vec(-3, 0, 0)
ball.v = vec(0, 0, 0)
ball.a = vec(0.35, 0, 0)

t = 0
dt = 0.01

# 속도 벡터
attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)

# 자취
attach_trail(ball, type='points', pps=5)

# 시뮬레이션
while t < 5:
	rate(1 / dt)

	ball.v = ball.v + ball.a * dt
	ball.pos = ball.pos + ball.v * dt

	t = t + dt
