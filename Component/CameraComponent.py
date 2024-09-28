from Managers.SceneManager import SceneManager
from Component.Component import Component
from pygame import Surface
from Objects.Actor import Actor


class CameraComponent(Component):
	def init(self):
		super().init()

	def update(self):
		super().update()

		if not isinstance(self.owner, Actor):
			return

		pos = self.owner.getPos()
		SceneManager.GI().setCameraPos(pos)

	def render(self, display: Surface):
		super().render(display)
