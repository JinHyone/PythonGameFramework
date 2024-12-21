from vpython import *


# 초기화
balls = []

ball1 = sphere(radius=0.2)
ball1.name = 'ball1'
ball1.pos = vector(-3, 3, 0)
ball1.v = vector(1, 0, 0)
ball1.a = vector(0, -2, 0)
balls.append(ball1)


ball2 = sphere(radius=0.2)
ball2.name = 'ball2'
ball2.pos = vector(3, 3, 0)
ball2.v = vector(0, 0, 0)
ball2.a = vector(0, -2, 0)
balls.append(ball2)


plate = box(width=10, height=0.3)
plate.rotate(3.141592 / 2, axis=vector(0, 1, 0))  # 라디안으로 회전
plate.pos = vector(0, -3, 0)

t = 0
dt = 0.016  # 60fps
c = 0  # 충돌한 물체 수


def collision(ball):
	global c
	r = ball.radius
	height = plate.height

	if r + height > abs(ball.pos.y - plate.pos.y):
		print(f'{ball.name}(time={t})')
		c += 1


# 시뮬레이션
while True:
	rate(1 / dt)

	if c == 2:
		break

	for ball in balls:
		collision(ball)
		ball.v = ball.v + ball.a * dt
		ball.pos = ball.pos + ball.v * dt

	t = t + dt

