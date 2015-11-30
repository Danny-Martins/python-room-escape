# for debug ignore
# import code;code.interact(local=vars())
from threading import Timer
import random
import time
import os

class makeRoom(object):
	def __init__(self, name, items=None, locked=None):
		self.items = items or []
		self.name = name
		self.locked = locked

	def __repr__(self):
		return self.name

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
		print('You are in %s.' % self.position.name)

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

	def grid_move(self, choice):
		self.move_items(choice)
		if choice == "n" and self.x !=0 and all_rooms[self.x - 1][self.y].locked != True:
			self.x -= 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "e" and self.y !=2 and all_rooms[self.x][self.y + 1].locked != True:
			self.y += 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "s" and self.x !=3 and all_rooms[self.x + 1][self.y].locked != True:
			self.x += 1
			self.position = all_rooms[self.x][self.y]
		elif choice == "w" and self.y !=0 and all_rooms[self.x][self.y - 1].locked != True:
			self.y -= 1
			self.position = all_rooms[self.x][self.y]
		else:
			print("locked or you typed something wrong")

# how the game must be layed out,  
# item 1 in room a , item 1 used in room B which unlocks C 
# item 2 in room c , item 2 used in room D which drops item 3
# item 4 in room E, unlocks F , room F leads to final room
# item 3 used in final room

room_a = makeRoom("Room A", ["rope"])
room_b = makeRoom("Room B")
room_c = makeRoom("Room C", ["knife"], True)
room_d = makeRoom("Room D")
room_e = makeRoom("Room E", ["crowbar"])
room_f = makeRoom("Room F", ["test"], True)
room_g = makeRoom("Room G")
room_h = makeRoom("Room H")
room_i = makeRoom("Room I")
room_j = makeRoom("Room J")
room_k = makeRoom("Room K")
room_final = makeRoom("Room final", ["test"], True)

random_rooms = [room_a, room_b, room_g, room_d, room_e, room_h, room_i, 
				room_j, room_k]
random.shuffle(random_rooms)

first_room_row = [random_rooms[0],random_rooms[1],random_rooms[2]]
second_room_row = [random_rooms[3],random_rooms[4],random_rooms[5]]
third_room_row = [random_rooms[6],random_rooms[7],random_rooms[8]]
final_room_row = [room_c, room_f, room_final]

all_rooms = []
all_rooms.append(first_room_row)
all_rooms.append(second_room_row)
all_rooms.append(third_room_row)
all_rooms.append(final_room_row)

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
