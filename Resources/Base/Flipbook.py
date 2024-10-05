from Resources.ResourceBase import ResourceBase
from Resources.Base.Texture import Texture
from pygame import Vector2


class FlipbookInfo:
	texture: Texture = None
	name: str = ''
	size: Vector2 = Vector2(0, 0)
	start: int = 0
	end: int = 0
	line: int = 0
	duration: float = 1
	loop: bool = True


class Flipbook(ResourceBase):
	info: FlipbookInfo = FlipbookInfo()

	def setFlipbookInfo(self, info: FlipbookInfo):
		self.info = info

	def getFlipbookInfo(self) -> FlipbookInfo:
		return self.info
