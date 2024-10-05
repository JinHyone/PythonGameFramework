from Resources.Base.Texture import SCALING_FLAG
from Scene.Scene import Scene, SCENE_TYPE
from Objects.Actor import Actor, ACTOR_TYPE
from Managers.ResourceManager import ResourceManager
from Resources.Base.Flipbook import Flipbook, FlipbookInfo
from pygame import Vector2, Vector3


class GameScene(Scene):
	def __init__(self):
		super().__init__(SCENE_TYPE.GAME_SCENE)

	def init(self):
		from Component.CameraComponent import CameraComponent
		from Objects.SpriteActor import SpriteActor
		from Objects.FlipbookActor import FlipbookActor
		back_t = ResourceManager.GI().LoadTexture('background_t', 'py_back_HD.jpg', (0, 0, 0))
		back_t.scaling(0.65, 0.65, SCALING_FLAG.RATIO)
		back_s = ResourceManager.GI().createSprite('back_s', back_t, 0, 0, 0, 0)
		back = SpriteActor(Vector3(0, 0, 0), ACTOR_TYPE.BACKGROUND)
		back.setSprite(back_s)
		self.add_actor(back)

		player_t = ResourceManager.GI().LoadTexture('actor_t', 'Actor2.png', (0, 0, 0))
		player_f = ResourceManager.GI().createFlipbook('actor_f')
		info = FlipbookInfo()
		info.start = 0
		info.loop = True
		info.texture = player_t
		info.end = 8
		info.size = Vector2(64, 64)
		info.duration = 2
		info.name = 'actor'
		info.line = 2
		info.texture = player_t
		player_f.setFlipbookInfo(info)

		player = FlipbookActor(Vector3(0, 0, 0), ACTOR_TYPE.PLAYER)
		player.setFlipbook(player_f)
		player.addComponent(CameraComponent())

		self.add_actor(player)

	def update(self):
		super().update()

	def render(self, display):
		super().render(display)

	def add_actor(self, actor: Actor):
		super().add_actor(actor)

	def remove_actor(self, actor: Actor):
		super().remove_actor(actor)
