from enum import Enum, auto
from numpy import array, append, delete
from numpy.typing import NDArray

from Objects.Actor import Actor
from Managers.TimeManager import TimeManager

class SCENE_TYPE(Enum):
	NONE       = auto()
	GAME_SCENE = auto()
	DEV_SCENE  = auto()


# 게임이 진행되는 메인 공간
class Scene:
	type: SCENE_TYPE

	def __init__(self, scene_type: SCENE_TYPE):
		self.actors: NDArray[Actor] = array([])
		self.type: SCENE_TYPE = scene_type

	def init(self):
		pass

	def update(self):
		for actor in self.actors:
			actor.update()

	def render(self, display):
		for actor in self.actors:
			actor.render(display)

	def add_actor(self, actor: Actor):
		self.actors = append(self.actors, actor)

	def remove_actor(self, actor: Actor):
		delete(self.actors, actor)