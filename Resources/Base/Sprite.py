from pygame import Surface, Vector2, Vector3, Color

from Resources.Base.Texture import Texture
from Resources.ResourceBase import ResourceBase


class Sprite(ResourceBase):
	texture: Texture
	x: int
	y: int
	cx: int
	cy: int

	def __init__(self, texture: Texture, x: int | None, y: int | None, cx: int | None, cy: int | None):
		self.texture = texture

		if x is None or y is None or cx is None or cy is None:
			self.x = 0
			self.y = 0
			self.cx = texture.getWidth()
			self.cy = texture.getHeight()

			return

		self.x = x
		self.y = y
		self.cx = cx
		self.cy = cy

	def getSurface(self) -> Surface:
		return self.texture.getSurface()

	def getTransparent(self) -> Color | tuple[int, int, int]:
		return self.texture.getTransparent()

	def getPos(self) -> Vector3:
		return Vector3(self.x, self.y, 0)

	def getSize(self) -> Vector2:
		return Vector2(self.cx, self.cy)
