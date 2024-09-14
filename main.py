import pygame
from pygame import init, display
from pygame.color import THECOLORS
from Managers.InputManager import InputManager
from Managers.TimeManager import TimeManager
from Managers.SceneManager import SceneManager

# constant config
FPS: int = 60
display_width = 1280
display_height = 720

init()  # pygame init
TimeManager.GI().setFPS(FPS)

GameDisplay = display.set_mode((display_width, display_height), pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.HWSURFACE)
GameDisplay.fill(THECOLORS['white'])

display.set_caption('Game')

background = pygame.transform.scale(pygame.image.load('E:/PythonProject/HanyangGameProject/Resources/py_back_HD.jpg'),
                                    (display_width, display_height))
fi = pygame.image.load('E:/PythonProject/HanyangGameProject/Resources/fi.png')


def GameMain():
	GameDisplay.blit(background, (0, 0))
	GameDisplay.blit(fi, (500, 100))
	display.flip()


while True:
	InputManager.GI().update()
	TimeManager.GI().update()
	SceneManager.GI().update()
	SceneManager.GI().render(GameDisplay)

	if InputManager.GI().KeyPressed('f'):
		print('fps: {} delta: {}'.format(TimeManager.GI().getFrame(), TimeManager.GI().getDelta()))

	GameMain()
