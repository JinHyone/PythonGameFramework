from Objects.Actor import Actor, ACTOR_TYPE
from Resources.Base.Flipbook import Flipbook
from pygame import Surface, Vector3, Rect
from Managers.TimeManager import TimeManager
from Managers.SceneManager import SceneManager


class FlipbookActor(Actor):
	flipbook: Flipbook
	sum_time: float = 0
	idx: int = 0

	def __init__(self, pos: Vector3, actor_type: ACTOR_TYPE):
		super().__init__(pos, actor_type)

	def init(self):
		super().init()

	def update(self):
		super().update()

		if not isinstance(self.flipbook, Flipbook):
			return

		info = self.flipbook.getFlipbookInfo()
		if info.loop is False and self.idx == info.end:
			return

		deltaTime = TimeManager.GI().getDelta()
		self.sum_time += deltaTime

		frameCount = (info.end - info.start) + 1
		delta = info.duration / frameCount

		if self.sum_time >= delta:
			self.sum_time -= delta
			self.idx = (self.idx + 1) % frameCount

	def render(self, display: Surface):
		super().render(display)

		if not isinstance(self.flipbook, Flipbook):
			return

		windowSize = display.get_size()
		info = self.flipbook.getFlipbookInfo()
		pos = self.pos
		cameraPos = SceneManager.GI().getCameraPos()

		display.blit(info.texture.getSurface(),
		             [pos.x - info.size.x / 2 - (cameraPos.x - windowSize[0] / 2),
		              pos.y - info.size.y / 2 - (cameraPos.y - windowSize[1] / 2)],
		             Rect((info.start + self.idx) * info.size.x, info.line * info.size.y, info.size.x, info.size.y))

	def setFlipbook(self, flipbook: Flipbook):
		self.flipbook = flipbook

	def reset(self):
		pass

	def isAnimationEnded(self) -> bool:
		pass
