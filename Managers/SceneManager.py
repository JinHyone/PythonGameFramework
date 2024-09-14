from pygame import Vector3
from typing import Optional

from Scene.Scene import Scene, SCENE_TYPE
from Scene.Game.GameScene import GameScene


class SceneManager:
	scene: Optional[Scene] = None
	sceneType: SCENE_TYPE = None
	instance: 'SceneManager' = None
	camera_pos: Vector3 = Vector3(0, 0, 0)

	@staticmethod
	# GetInstance Method 싱글톤
	def GI() -> Optional['SceneManager']:
		if SceneManager.instance is None:
			SceneManager.instance = SceneManager()
			SceneManager.instance.init()

		return SceneManager.instance

	def init(self):
		self.changeScene(SCENE_TYPE.GAME_SCENE)

	def update(self):
		if self.scene is not None:
			self.scene.update()

	def render(self, display):
		if self.scene is not None:
			self.scene.render(display)

	def clear(self):
		if self.scene is not None:
			del self.scene
			self.scene = None

	def changeScene(self, scene_type: SCENE_TYPE) -> Scene:
		newScene: Optional[Scene] = None

		match scene_type:
			case SCENE_TYPE.GAME_SCENE:
				newScene = GameScene()

			case _:
				pass

		self.clear()
		self.scene = newScene
		self.scene.init()
		return self.scene

	def getCurrentScene(self) -> Scene:
		return self.scene

	def getCameraPos(self) -> Vector3:
		return self.camera_pos

	def setCameraPos(self, pos: Vector3):
		self.camera_pos = pos
