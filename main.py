from pygame import init, display, Vector3, DOUBLEBUF, FULLSCREEN, HWSURFACE
from pygame.color import THECOLORS
from Managers.InputManager import InputManager
from Managers.TimeManager import TimeManager
from Managers.SceneManager import SceneManager
from Objects.Actor import ACTOR_TYPE
from Objects.SpriteActor import SpriteActor
from Resources.Base.Sprite import Sprite
from Resources.Base.Texture import Texture, SCALING_FLAG
from Component.CameraComponent import CameraComponent

# constant config
FPS: int = 60
display_width = 1280
display_height = 720

init()  # pygame init
TimeManager.GI().setFPS(FPS)

GameDisplay = display.set_mode((display_width, display_height), DOUBLEBUF | HWSURFACE)
GameDisplay.fill(THECOLORS['white'])

display.set_caption('Game')

background_texture = Texture()
background_texture.loadImage('E:/PythonProject/HanyangGameProject/Resources/py_back_HD.jpg')
background_texture.scaling(display_width, display_height, SCALING_FLAG.ABSOLUTE)

background = SpriteActor(Vector3(0, 0, 0), ACTOR_TYPE.BACKGROUND)
background.setSprite(Sprite(background_texture, None, None, None, None))


fi_texture = Texture()
fi_texture.loadImage('E:/PythonProject/HanyangGameProject/Resources/fi.png')
fi_texture.scaling(0.5, 0.5, SCALING_FLAG.RATIO)


actor1 = SpriteActor(Vector3(100, 80, 0), ACTOR_TYPE.PLAYER)
actor1.setSprite(Sprite(fi_texture, None, None, None, None))

camera = CameraComponent()
actor1.addComponent(camera)

SceneManager.GI().getCurrentScene().add_actor(background)

SceneManager.GI().getCurrentScene().add_actor(actor1)
SceneManager.GI().setCameraPos(Vector3(0, 0, 0))


def GameMain():
	display.flip()


while True:
	InputManager.GI().update()
	TimeManager.GI().update()
	SceneManager.GI().update()
	SceneManager.GI().render(GameDisplay)

	if InputManager.GI().KeyPressed('f'):
		print('fps: {} delta: {}'.format(TimeManager.GI().getFrame(), TimeManager.GI().getDelta()))

	if InputManager.GI().KeyPressed(''):
		quit(0)
		exit(0)

	GameMain()
