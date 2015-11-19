from random import randint
import time

class makeRoom(object):
	def __init__(self, name, item=None):
		self.name = name
		self.items = [item]
		self.exit_north = False
		self.exit_east = False
		self.exit_south = False
		self.exit_west = False

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

	def check_input(self, choice):
		if choice == "north" and self.position.exit_north == True:
			print("you escaped and won nigga")
			exit()
		elif choice == "east" and self.position.exit_east == True:
			print("you escaped and won nigga")
			exit()
		elif choice == "south" and self.position.exit_south == True:
			print("you escaped and won nigga")
			exit()
		elif choice == "west" and self.position.exit_west == True:
			print("you escaped and won nigga")
			exit()
		elif choice == "take":
			item_choice = input("Choose item to pick up: ")
			try:
				temp_item = self.position.items.index(item_choice)
				temp_item = self.position.items[temp_item]
				print("you picked up %s and put it in your backpack" % temp_item)
				self.backpack.append(temp_item)
				self.position.items.remove(temp_item)
				time.sleep(2)
			except ValueError:
				print("that wasnt an item dipshit \n")
				time.sleep(2)
		else:
			print("you typed something wrong")

room_start = makeRoom("the starter room","Sword")
flamie = player(room_start)

while True:

	flamie.print_backpack()
	flamie.print_room_items()
	flamie.print_options()
	choice = input()
	flamie.check_input(choice)
