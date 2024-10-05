from typing import Optional
from pygame import Surface, Color

from Resources.Base.Texture import Texture
from Resources.Base.Sprite import Sprite
from Resources.Base.Flipbook import Flipbook


class ResourceManager:
	instance: 'ResourceManager' = None
	display: Surface = None
	resourcePath: str = ''
	textures: dict[str, Texture] = dict()
	sprites: dict[str, Sprite] = dict()
	flipbooks: dict[str, Flipbook] = dict()

	@staticmethod
	# GetInstance Method 싱글톤
	def GI() -> Optional['ResourceManager']:
		if ResourceManager.instance is None:
			ResourceManager.instance = ResourceManager()
			ResourceManager.instance.init()

		return ResourceManager.instance

	def init(self):
		pass

	def clear(self):
		for item in self.textures:
			del self.textures[item]

		for item in self.flipbooks:
			del self.flipbooks[item]

		for item in self.sprites:
			del self.sprites[item]

	def getTexture(self, key: str):
		pass

	def LoadTexture(self, key: str, path: str, transparent: tuple[int, int, int] | Color):
		if self.textures.get(key) is not None:
			return self.textures.get(key)

		fullpath = self.resourcePath + path  # C:/..../file/resource/
		texture = Texture()
		texture.loadImage(fullpath)
		texture.setTransparent(transparent)
		self.textures[key] = texture

		return texture

	def getSprite(self, key: str):
		return self.sprites.get(key)

	def createSprite(self, key: str, texture: Texture, x: int, y: int, cx: int, cy: int):
		if self.sprites.get(key) is not None:
			return self.sprites.get(key)

		if cx == 0:
			cx = texture.getWidth()

		if cy == 0:
			cy = texture.getHeight()

		sprite = Sprite(texture, x, y, cx, cy)
		self.sprites[key] = sprite

		return sprite

	def getFlipbook(self, key: str):
		return self.flipbooks.get(key)

	def createFlipbook(self, key: str):
		if self.flipbooks.get(key) is not None:
			return self.flipbooks.get(key)

		fb = Flipbook()
		self.flipbooks[key] = fb

		return fb

	def setResourcePath(self, resourcePath: str):
		self.resourcePath = resourcePath

	def setDisplay(self, display: Surface):
		self.display = display

	def getResourcePath(self) -> str:
		return self.resourcePath
