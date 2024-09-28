from pygame import Vector3, Surface
from enum import Enum, auto
from numpy import array, insert, delete, where
from numpy.typing import NDArray
from typing import TYPE_CHECKING


class ACTOR_TYPE(Enum):
	BACKGROUND = auto(),
	PLAYER = auto()


# 더 추가 예정


if TYPE_CHECKING:
	from Component.Component import Component


# Actor(씬에 배치되는 가장 기본이 되는 오브젝트) 클래스 추상화
class Actor:
	pos: Vector3
	type: ACTOR_TYPE

	def __init__(self, pos: Vector3, actor_type: ACTOR_TYPE):
		self.pos = pos
		self.type = actor_type
		from Component.Component import Component
		self.components: NDArray[Component] = array([], dtype=Component)

	def init(self):
		for component in self.components:
			component.init()

	def update(self):
		for component in self.components:
			component.update()

	def render(self, display: Surface):
		for component in self.components:
			component.render(display)

	def addComponent(self, component: 'Component'):
		component.init()
		component.setOwner(self)
		self.components = insert(self.components, len(self.components), [component])

	def removeComponent(self, component: 'Component'):
		delete(self.components, where(self.components == component))

	def getPos(self) -> Vector3:
		return self.pos

	def setPos(self, pos: Vector3):
		self.pos = pos
