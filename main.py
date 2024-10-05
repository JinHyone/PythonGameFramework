import pygame
from pygame import init, display, Vector3, DOUBLEBUF, FULLSCREEN, HWSURFACE, Rect
from pygame.color import THECOLORS
from Managers.InputManager import InputManager
from Managers.TimeManager import TimeManager
from Managers.SceneManager import SceneManager
from Managers.ResourceManager import ResourceManager

# constant config
FPS: int = 1000
display_width = 1280
display_height = 720

init()  # pygame init
TimeManager.GI().setFPS(FPS)

GameDisplay = display.set_mode((display_width, display_height), DOUBLEBUF | HWSURFACE)
GameDisplay.fill(THECOLORS['white'])

ResourceManager.GI().init()
ResourceManager.GI().setResourcePath('E:/PythonProject/HanyangGameProject/Resources/')
ResourceManager.GI().setDisplay(GameDisplay)

SceneManager.GI().init()
display.set_caption('Game')

while True:
	GameDisplay.fill((255, 255, 255), Rect((0, 0), (display_width, display_height)))
	InputManager.GI().update()
	TimeManager.GI().update()
	SceneManager.GI().update()
	SceneManager.GI().render(GameDisplay)

	if InputManager.GI().KeyPressed('f'):
		print('fps: {} delta: {}'.format(TimeManager.GI().getFrame(), TimeManager.GI().getDelta()))

	if InputManager.GI().KeyPressed(''):
		quit(0)
		exit(0)

	display.flip()
