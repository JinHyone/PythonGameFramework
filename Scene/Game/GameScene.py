from Scene.Scene import Scene, SCENE_TYPE
from Objects.Actor import Actor


class GameScene(Scene):
	def __init__(self):
		super().__init__(SCENE_TYPE.DEV_SCENE)

	def update(self):
		super().update()
		print('game scene update')

	def render(self, display):
		super().render(display)
		print('game scene render')

	def add_actor(self, actor: Actor):
		super().add_actor(actor)

	def remove_actor(self, actor: Actor):
		super().remove_actor(actor)