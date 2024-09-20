from pygame import Surface, Vector3

from Texture import Texture
from Resources.ResourceBase import ResourceBase


class Sprite(ResourceBase):
	texture: Texture
	x: int
	y: int
	cx: int
	cy: int

	def __init__(self, texture: Texture, x: int, y: int, cx: int, cy: int):
		pass

	def getSurface(self) -> Surface:
		return self.texture.surface

	def getTransparent(self):
		return self.texture.getTransparent()

	def getPos(self):
		return Vector3(self.x, self.y, 0)

	def getSize(self):
		return Vector3(self.cx, self.cy, 0)
