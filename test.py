import sys
import Duty

    
# def main ():
#     name = sys.argv[1] 
#     file_name=len(name)
#     add_rooms()
#     load_room_from_file()

#     if file_name > 1:
#         def load_room_from_file(file_name: str)-> (list[str] | None):
#             file_handle = open(file_name, "r")
#             while True:
#                 room_specs=file_handle.readlines()
#                 if room_specs == "":
#                     break
#                 return room_specs
#             file_handle.close()

#     # this function divides the things in our files in two between room name and items
#         def room_specs():
#             room = {}
#             for line in room_specs:
#                 #divides the file between room and items acording to ':'
#                 room_and_items=line.strip().split(':')
#                 if len(room_and_items)==2:
                    
#                     room_name=room_and_items[0].strip()
#                     #split items with a comma
#                     item=[item.strip() for item in room_and_items[1].split(',')]
#                     room[room_name]=item
#                 else:
#                     print(f"Error: Invalid format in line - {line}")
#                     return {}
#             return room
#         # Duty.add_room(room[0], room[2])
#         def add_rooms(room:(str,[str])):
#             for room_name, item in room.item():
#                 Duty.add_room(room_name, item)

#                 print("good")
#     else:
#         print("oh no")
# main()

#-----------------------------------------------------------------------------------
#IMPORTANT COMMENTS TO ADD
# def main():

# def add_rooms():
#     """
#     Adds all of the rooms to the game. 
#     Duty.add_room() takes a string for the name of a room and a list of strings for the items in the room.

#     """
#     if len(sys.argv)>1:
#         file_name=sys.argv[1]
#         return file_name
#     else:
#         Duty.add_room("Living Room", ["42\" TV Playing Golf", "Black Leather Sofa", "Circular Metal Coffee Table", "Wooden Bookshelf with 3 Shelves"])
#         Duty.add_room("Kitchen", ["Gas Stove", "Retro Red Metal Refrigerator", "Oak Wooden Table", "4 Wooden Chairs"])
#         Duty.add_room("Bedroom", ["Queen Size Bed", "Oak Wooden Nightstand", "Oak Wooden Dresser", "Oak Wooden Desk", "Oak Wooden Chair"])
#         Duty.add_room("Bathroom", ["Toilet with Oak Seat", "Chrome Sink", "Shower with Blue Tiles", "Medicine Cabinet"])
#         return None
# # scan through
#         #file_handle.readline
#         #While loop to scan the file
#         #room name, itemlist[i]
#         #for i loop range(load_room_from_file(file_name))]
#         # Duty.add_room(room[0], room[2])
#         # all character before ":" is room name
#         # after ":" list, each "," append on list
#         # room ["string", items[]]
#         # return how many rooms

# def load_room_from_file(file_name: str) -> list[str]:
#     try:
#         with open(file_name, "r") as file_handle:
#             room_specs = file_handle.readline()
#         return room_specs
#     except FileNotFoundError:
#         print(f"Error: File not found - {file_name}")
#         return []
#     except Exception as e:
#         print(f"Error loading room data: {e}")
#         return []

#     # this function divides the things in our files in two between room name and items
# def room_specs(room_specs:list[str])->[str, list[str]]:
#     room = {}
#     for line in room_specs:
#         #divides the lines it's reading in to between room name and imest in that room
#         room_and_items=line.strip().split(':')
#         #checks if the line has been divided in two
#         if len(room_and_items)==2:
#             room_name=room_and_items[0].strip()
#             room_content=[item.strip() for item in room_and_items[1].split(',')]
#             room[room_name]=room_content
#         else:
#             print(f"Error: Invalid format in line - {line}")
#             return {}
#     return room
#         # Duty.add_room(room[0], room[2])
# def creat_room(room:tuple[str, list[str]]):
#     room_name, items = room
#     Duty.add_room(room_name, items)
#         #room name, itemlist[i]
#         # for i loop range(load_room_from_file(file_name))
        
#         # Duty.add_room(room[0], room[2])
#     # If there is none, load the defaultq
#     # Scan through the TXT file
#     # A list of room names with items
#     # room number > anomalies

# main()
#------------------------------------------------------

import sys
def main():
    if len(sys.argv) > 1:
        load_room_from_file(sys.argv[1])
    else:
        print ("No argument!")
def load_room_from_file (file_name: str) -> list:
    file_handle = open(file_name,"r")
    room_list = []
    # iterate through all the lines
    # Remove the "" and "\n"
    # And append it in our list
    for rooms in file_handle.readlines():
        room_list.append(rooms.rstrip('\n').split(":"))
# iterate through lenght of our room_list
# Remove all ","
    for item_lists in range(len(room_list)): 
        x= room_list[item_lists][1].split(",")
        room_list[item_lists][1] = x

    print(Duty.add_room(room_list))
    return room_list
main()



