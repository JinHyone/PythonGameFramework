from pygame.image import load
from pygame.transform import scale
from pygame.surface import Surface
from pygame.color import Color
from enum import Enum, auto


class SCALING_FLAG(Enum):
	RATIO = auto(),
	ABSOLUTE = auto()


class Texture:
	surface: Surface
	transparent: Color | tuple[int, int, int] = (0, 255, 0)
	width: int | float
	height: int | float

	def loadImage(self, path: str) -> 'Texture':
		self.surface = load(path).convert_alpha()
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
		# self.surface.set_colorkey(color)

	def getTransparent(self) -> Color | tuple[int, int, int]:
		return self.transparent

	def scaling(self, sx: float | int, sy: float | int, flag: SCALING_FLAG):
		if flag == SCALING_FLAG.RATIO:
			self.surface = scale(self.surface, [self.width * sx, self.height * sy])
			self.width = self.width * sx
			self.height = self.height * sy

		elif flag == SCALING_FLAG.ABSOLUTE:
			self.surface = scale(self.surface, [sx, sy])
			self.width = sx
			self.height = sy

