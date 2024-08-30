from pygame.time import Clock


class TimeManager:
	deltaTime: float
	clock: Clock
	FPS: int = 60
	instance: 'TimeManager' = None

	@staticmethod
	# GetInstance Method
	def GI():
		if TimeManager.instance is None:
			TimeManager.instance = TimeManager()
			TimeManager.instance.init()

		return TimeManager.instance

	def init(self):
		self.deltaTime = 0
		self.clock = Clock()

	def update(self):
		self.deltaTime = self.clock.tick(self.FPS) / 1000

	def setFPS(self, fps: int):
		self.FPS = fps

	def getDelta(self):
		return self.deltaTime

	def getFrame(self):
		return self.clock.get_fps()
