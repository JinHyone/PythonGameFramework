from Scene import Scene
from Objects.Actor import Actor


class GameScene(Scene):
	def __init__(self):
		super().__init__()

	def update(self):
		super().update()

	def render(self):
		super().update()

	def add_actor(self, actor: Actor):
		super().add_actor(actor)

	def remove_actor(self, actor: Actor):
		super().remove_actor(actor)