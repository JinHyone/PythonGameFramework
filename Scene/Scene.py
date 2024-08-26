from enum import Enum, auto
from numpy import array, append, delete
from numpy.typing import NDArray

from Objects.Actor import Actor


class SCENE_TYPE(Enum):
	NONE       = auto()
	GAME_SCENE = auto()
	DEV_SCENE  = auto()


# 게임이 진행되는 메인 공간
class Scene:
	def __init__(self):
		self.actors: NDArray[Actor] = array([])
		self.sceneType: SCENE_TYPE = SCENE_TYPE.NONE

	def update(self):
		for actor in self.actors:
			actor.update()

	def render(self):
		for actor in self.actors:
			actor.render()

	def add_actor(self, actor: Actor):
		self.actors = append(self.actors, actor)

	def remove_actor(self, actor: Actor):
		delete(self.actors, actor)