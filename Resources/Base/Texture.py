from pygame.image import load
from pygame.surface import Surface
from pygame.color import Color


class Texture:
	surface: Surface
	transparent: Color | tuple[int, int, int] = (0, 255, 0)
	width: int
	height: int

	def loadImage(self, path: str) -> 'Texture':
		self.surface = load(path)
		size = self.surface.get_size()

		self.width = size[0]
		self.height = size[1]

		return self

	def getSurface(self) -> Surface:
		return self.surface

	def getWidth(self) -> int:
		return self.width

	def getHeight(self) -> int:
		return self.height

	def setTransparent(self, color: Color | tuple[int, int, int]):
		self.transparent = color

	def getTransparent(self) -> Color | tuple[int, int, int]:
		return self.transparent
