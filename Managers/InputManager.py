from sys import exit
from typing import Dict

import pygame
from pygame import event, quit, QUIT, KEYDOWN, KEYUP


class InputManager:
	key: Dict[str, bool] = dict()
	instance: 'InputManager' = None

	@staticmethod
	# GetInstance Method
	def GI():
		if InputManager.instance is None:
			InputManager.instance = InputManager()

		return InputManager.instance

	def KeyPressed(self, key_type):
		return self.key.get('d')

	def update(self):
		for ev in event.get():
			if ev.type == QUIT:
				quit()
				exit()
			elif ev.type == KEYDOWN:
				key = ev.key if ev.key > 1000 else chr(ev.key)
				self.key[key] = True

			elif ev.type == KEYUP:
				key = ev.key if ev.key > 1000 else chr(ev.key)
				self.key[key] = False

				if True in [v for k, v in self.key.items() if v]:
					return
