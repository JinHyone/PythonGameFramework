from pygame import init, display
from pygame.color import THECOLORS
from Managers.InputManager import InputManager

# constant config
FPS: int = 60

init()

GameDisplay = display.set_mode((720, 1080))
GameDisplay.fill(THECOLORS['white'])

display.set_caption('Game')


def GameMain():
	GameDisplay.fill(THECOLORS['white'])


while True:
	display.update()
	InputManager.GI().update()
	GameMain()

