from vpython import *


# 초기화
ball = sphere(radius=0.2)

ball.pos = vector(0, 3, 0)
ball.v = vector(0, 0, 0)
ball.a = vector(0, -2, 0)


plate = box(width=5, height=0.3)
plate.rotate(3.141592 / 2, axis=vector(0, 1, 0))  # 라디안으로 회전
plate.pos = vector(0, -3, 0)

t = 0
dt = 0.016


def collision():
	r = ball.radius
	height = plate.height

	if ball.v.dot(ball.pos - plate.pos) > 0:  # 오류 방지를 위해서 멀어지면 충돌체크 x
		return

	if r + height > mag(ball.pos - plate.pos):
		ball.v *= -0.8


# 시뮬레이션
while True:
	rate(1 / dt)
	collision()

	ball.v = ball.v + ball.a * dt
	ball.pos = ball.pos + ball.v * dt

	t = t + dt

