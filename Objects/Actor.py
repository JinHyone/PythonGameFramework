from pygame import Vector3
from enum import Enum, auto


class ACTOR_TYPE(Enum):
	PLAYER = auto()
	# 더 추가 예정


# Actor(씬에 배치되는 가장 기본이 되는 오브젝트) 클래스 추상화
class Actor:
	def __init__(self):
		self.pos: Vector3 = Vector3()

	def update(self):
		pass

	def render(self):
		pass
