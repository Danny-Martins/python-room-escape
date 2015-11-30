# for debug ignore
# import code;code.interact(local=vars())
from threading import Timer
import random
import time
import os

class makeRoom(object):
	def __init__(self, name, items=None):
		self.items = items or []
		self.name = name
		self.exit_north = None
		self.exit_east = None
		self.exit_south = None
		self.exit_west = None

	def __repr__(self):
		return self.name

	# legacey code , more for testing at this point
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
		self.x = 0
		self.y = 1

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

	def grid_move(self, choice):
		self.move_items(choice)
		if choice == "north" and self.x !=0:
			self.x -= 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "east" and self.y !=2:
			self.y += 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "south" and self.x !=1:
			self.x += 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "west" and self.y !=0:
			self.y -= 1
			self.position = all_rooms[self.x][self.y]
		else:
			print("locked or you typed something wrong")

# how the game must be layed out,  
# item 1 in room a , item 1 used in room b which unlocks c 
# item 2 in room c , item 2 used in room D which drops item 3
# item 4 in room E, unlocks F , room F leads to final room
# item 3 used in final room

room_a = makeRoom("Room A", ["Rope"])
room_b = makeRoom("Room B")
room_c = makeRoom("Room C", ["Knife"])
room_d = makeRoom("Room D")
room_e = makeRoom("Room E", ["Crowbar"])
room_f = makeRoom("Room F")

room_test1 = makeRoom("test1")
room_test2 = makeRoom("test2")

random_rooms = [room_a, room_b, room_c, room_d, room_e, room_f]
random.shuffle(random_rooms)

first_room_row = [random_rooms[0],random_rooms[1],random_rooms[2]]
second_room_row = [random_rooms[3],random_rooms[4],random_rooms[5]]

all_rooms = []
all_rooms.append(first_room_row)
all_rooms.append(second_room_row)

flamie = player(all_rooms[0][1])

while True:

	os.system("cls")
	print(flamie.x)
	print(flamie.y)
	flamie.print_backpack()
	flamie.print_room_items()
	flamie.print_options()
	choice = input()
	# flamie.check_input(choice)
	flamie.grid_move(choice)
