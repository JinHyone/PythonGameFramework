from sys import exit
from typing import Dict

import pygame
from pygame import event, quit, QUIT, KEYDOWN, KEYUP


class InputManager:
	key: Dict[int, bool] = dict()
	instance: 'InputManager' = None

	@staticmethod
	# GetInstance Method
	def GI():
		if InputManager.instance is None:
			InputManager.instance = InputManager()

		return InputManager.instance

	def KeyPressed(self, key_type):
		if True in [v for k, v in self.key.items() if k == key_type]:
			return True
		return False

	def update(self):
		for ev in event.get():
			if ev.type == QUIT:
				quit()
				exit()
			elif ev.type == KEYDOWN:
				self.key[ev.key] = True

			elif ev.type == KEYUP:
				self.key[ev.key] = False
				if True in [v for k, v in self.key.items() if v]:
					return
