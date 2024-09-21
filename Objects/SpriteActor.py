from pygame import Vector3, Surface, Rect
from Resources.Base.Sprite import Sprite
from Managers.SceneManager import SceneManager

from Objects.Actor import Actor, ACTOR_TYPE


class SpriteActor(Actor):
	sprite: Sprite

	def __init__(self, pos: Vector3, actor_type: ACTOR_TYPE):
		super().__init__(pos, actor_type)

	def init(self):
		super().init()

	def update(self):
		super().update()

	def render(self, display: Surface):
		super().render(display)

		if not isinstance(self.sprite, Sprite):
			return

		pos = self.pos
		size: Vector3 = self.sprite.getSize()
		cameraPos: Vector3 = SceneManager.GI().getCameraPos()
		windowSize = display.get_size()

		display.blit(self.sprite.getSurface(), [pos.x - size.x / 2 - (cameraPos.x - windowSize[0] / 2),
		                                        pos.y - size.y / 2 - (cameraPos.y - windowSize[1] / 2)],
		             Rect(self.sprite.x, self.sprite.y, self.sprite.cx, self.sprite.cy))

	def setSprite(self, sprite: Sprite):
		self.sprite = sprite
