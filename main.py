from pygame import init, display
from pygame.color import THECOLORS
from Scene.Scene import SCENE_TYPE
from Managers.InputManager import InputManager
from Managers.TimeManager import TimeManager
from Managers.SceneManager import SceneManager

# constant config
FPS: int = 60

init()  # pygame init
TimeManager.GI().setFPS(250)

GameDisplay = display.set_mode((1080, 720))
GameDisplay.fill(THECOLORS['white'])

display.set_caption('Game')


def GameMain():
	GameDisplay.fill(THECOLORS['white'])


while True:
	InputManager.GI().update()
	TimeManager.GI().update()
	SceneManager.GI().update()
	SceneManager.GI().render(GameDisplay)

	if InputManager.GI().KeyPressed('d'):
		print('fps: {} delta: {}'.format(TimeManager.GI().getFrame(), TimeManager.GI().getDelta()))

	GameMain()
	display.update()
