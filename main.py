from threading import Timer
import random
import time
import os

class makeRoom(object):
	def __init__(self, name, item=None):
		self.name = name
		self.items = [item]
		self.exit_north = None
		self.exit_east = None
		self.exit_south = None
		self.exit_west = None

	def attach_next_to(self, parent_room):
		random_temp = random.randint(1,4)
		if random_temp == 1:
			self.exit_north = parent_room
			parent_room.exit_south = self
		elif random_temp == 2:
			self.exit_east = parent_room
			parent_room.exit_west = self
		elif random_temp == 3:
			self.exit_south = parent_room
			parent_room.exit_north = self
		else:
			self.exit_west = parent_room
			parent_room.exit_east = self

	# ignore this , used to test certain rooms without going thru game etc
	def attach_next_to_debug(self, parent_room):
		self.exit_south = parent_room
		parent_room.exit_north = self

class player(object):
	def __init__(self, position):
		self.position = position
		self.backpack = []

	def print_backpack(self):
		print("here are the items in your backpack:")
		for item in self.backpack:
			print(item)

	def print_options(self):
		print('You are in %s. Here are your options for exits:' % self.position.name)
		print(' \nnorth: %s, east: %s, south: %s, west: %s ,type take for pickup items' 
			% (self.position.exit_north, self.position.exit_east, self.position.exit_south ,self.position.exit_west))

	def print_room_items(self):
		print('these are the items in the room:')
		for item in self.position.items:
			print(item)

	def move_items(self,choice):
		if choice == "take":
			item_choice = input("Choose item to pick up: ")
			try:
				temp_item = self.position.items.index(item_choice)
				temp_item = self.position.items[temp_item]
				print("you picked up %s and put it in your backpack" % temp_item)
				self.backpack.append(temp_item)
				self.position.items.remove(temp_item)
				time.sleep(2.5)
			except ValueError:
				print("not an item on the ground")
				time.sleep(2.5)
		elif choice == "drop":
			item_choice = input("Choose item to drop: ")
			try:
				temp_item = self.backpack.index(item_choice)
				temp_item = self.backpack[temp_item]
				print("you took %s and put it on the ground" % temp_item)
				self.position.items.append(temp_item)
				self.backpack.remove(temp_item)
				time.sleep(2.5)
			except ValueError:
				print("not item in your backpack")
				time.sleep(2.5)

	def check_input(self, choice):
		self.move_items(choice)
		if choice == "north" and self.position.exit_north:
			self.position = self.position.exit_north
		elif choice == "east" and self.position.exit_east:
			self.position = self.position.exit_east
		elif choice == "south" and self.position.exit_south:
			self.position = self.position.exit_south
		elif choice == "west" and self.position.exit_west:
			self.position = self.position.exit_west
		else:
			print("you typed something wrong")

if __name__ == "__main__":

	room_start = makeRoom("the starter room","Sword")
	room_test = makeRoom("Room A","winrar.exe")
	room_test.attach_next_to(room_start)
	# flamie is my gamer tag being a game and being just a test 
	# before implimenting to HTML5 I named the player after myself
	flamie = player(room_start)

	while True:

		os.system("cls")
		flamie.print_backpack()
		flamie.print_room_items()
		flamie.print_options()
		choice = input()
		flamie.check_input(choice)
