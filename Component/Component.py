from pygame import Surface
from Objects.Actor import Actor


class Component:
	owner: Actor

	def init(self):
		pass

	def update(self):
		pass

	def render(self, display: Surface):
		pass

	def setOwner(self, owner: Actor):
		self.owner = owner

	def getOwner(self):
		return self.owner
