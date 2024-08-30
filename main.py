from pygame import init, display
from pygame.color import THECOLORS
from Managers.InputManager import InputManager
from Managers.TimeManager import TimeManager

# constant config
FPS: int = 60

init() # pygame init
TimeManager.GI().setFPS(250)

GameDisplay = display.set_mode((1080, 720))
GameDisplay.fill(THECOLORS['white'])

display.set_caption('Game')


def GameMain():
	GameDisplay.fill(THECOLORS['white'])


while True:
	display.update()
	InputManager.GI().update()
	TimeManager.GI().update()

	if InputManager.GI().KeyPressed('d'):
		print('fps: {} delta: {}'.format(TimeManager.GI().getFrame(), TimeManager.GI().getDelta()))

	GameMain()

