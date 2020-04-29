from django.contrib.auth.models import User
from adventure.models import Player, Room
import random
from algorithm.rooms import title, explanation
Room.objects.all().delete()
class World:
        def __init__(self):
            self.grid = None
            self.width = 0
            self.height = 0
        def generate_rooms(self, size_x, size_y, num_rooms):
            self.grid = [None] * size_y
            self.width = size_x
            self.height = size_y
            for i in range( len(self.grid) ):
                self.grid[i] = [None] * size_x
            x = -1 
            y = 0
            room_count = 0
            direction = 1
            previous_room = None
            while room_count < num_rooms:
                if direction > 0 and x < size_x - 1:
                    room_direction = "e"
                    x += 1
                elif direction < 0 and x > 0:
                    room_direction = "w"
                    x -= 1
                else:
                    room_direction = "n"
                    y += 1
                    direction *= -1
                room_title = random.choice(title)
                room_explanation = random.choice(explanation)
                room = Room(room_count, room_title, room_explanation, x, y)
                room.save()
                self.grid[y][x] = room
                if previous_room is not None:
                    previous_room.connectRooms(room, room_direction)
                previous_room = room
                room_count += 1
        def print_rooms(self):
            str = "# " * ((3 + self.width * 5) // 2) + "\n"
            reverse_grid = list(self.grid)
            reverse_grid.reverse()
            for row in reverse_grid:
                str += "#"
                for room in row:
                    if room is not None and room.n_to is not None:
                        str += "  |  "
                    else:
                        str += "     "
                str += "#\n"
                str += "#"
                for room in row:
                    if room is not None and room.w_to is not None:
                        str += "-"
                    else:
                        str += " "
                    if room is not None:
                        str += f"{room.id}".zfill(3)
                    else:
                        str += "   "
                    if room is not None and room.e_to is not None:
                        str += "-"
                    else:
                        str += " "
                str += "#\n"
                str += "#"
                for room in row:
                    if room is not None and room.s_to is not None:
                        str += "  |  "
                    else:
                        str += "     "
                str += "#\n"
            str += "# " * ((3 + self.width * 5) // 2) + "\n"
            print(str)



w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms()
print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
