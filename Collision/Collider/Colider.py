from enum import Enum, auto
from pygame import Surface


class ColliderType(Enum):
	Circle = auto()
	Rect = auto()
	none = auto()


class Collider:
	collider_type: ColliderType = ColliderType.none

	def __init__(self, collider_type: ColliderType):
		self.collider_type = collider_type

	def update(self):
		pass

	def render(self, display: Surface):
		pass
