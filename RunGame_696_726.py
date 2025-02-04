# 101324696 - SANTO MUKIZA
# 101318726 - JHERNIE MAGNAMPO
# Category 1: Add rooms from a file (please follow the conventions inside "rooms_with_items.txt")
# Category 2: Number anomaly
#       a. New anomaly - NUMBER DISTORTION
#       b. It checks if there is any numbers/digits in a random item in a room
#       c. All rooms need to have an item with number (having 4 maximum anomalies at a time will end the game without any error)

"""
Santo Mukiza

1. How did you pair program? 
    We collaborated in person at the library.
    
2. Did you work on any parts independently, and what parts if so?
    We both worked/researched on how to 
    a) read TXT files and store them as lists (including the clean-ups) 
    b) read through strings and find digits/numbers 
    c) practice using enumerate()
    
3. What tasks came up that were not planned in Assignment 8, if any?
    We discovered that you can read all lines in a TXT file in one line of Python code. 
    Additionally, we found it very helpful to use enumerate(), which allows you to return two values (the index and the value at that index).



4. About how often did you change who was driver and who was navigator?
    We switched roles at least once during every meeting.
        
5. If you were to pair program in the future, what might you change?
    I probably won't change anything, for the pair programming worked smoothly for both of us.

"""
import Duty
import random
import sys

def main():
    """
    The main function is mostly just here to setup the game and keep it running in a loop.
    It has a specific order of events that it follows.
    There are a lot of comments in here to help you understand what is going on, but 
    feel free to remove them if they impede your reading of the code.
    """

    # First, we set up all of the game data. 
    # This could have been done using the init() function's optional parameters,
    # but this should make it easier for you to modify it later.

    # These 'helper functions' just clean up the main function and make it more readable.
    # We need to add rooms to the game and we need to register what anomalies are possible.
    add_rooms()
    register_anomalies()

    # It might be cleaner to put all of these into their own helper function. Feel free to do that if you think it would be better!
    Duty.set_setting("debug", True) # Setting this to True will show additional information to help you debug new anomalies
    Duty.set_setting("timescale", 60)
    Duty.set_setting("probability", 0.1)
    Duty.set_setting("min_seconds_between_anomalies", 10*60)

    # Initialize the game with all of the data we've just set up.
    Duty.init()

    # This is the main game loop. It will run until the game_running variable is set to False.
    game_running = True
    while game_running:
        # The game keeps track of time while the player is idle, so it is possible we will need
        # to create multiple anomalies at a time the next time the player types a command.
        # `number_of_anomalies_to_create` also takes our probability setting into account.
        n_anomalies = Duty.number_of_anomalies_to_create()

        # We create one anomaly at a time, and we'll write a small helper function to clean up the main function.
        for _ in range(n_anomalies):
            # Keep looping until we can create the anomaly, just in case one of them fails
            anomaly_created = False
            while not anomaly_created:
                anomaly_created = create_anomaly()
            

        # This will update the game status to check if we've lost the game or reached the end.
        # Update returns True if the game should keep going or False if it should end after this loop.
        game_running = Duty.update()

        # Display shows all of the game data. If update() determined the game should end, display() will show the end screen.
        Duty.display()

        # This will pause the loop and wait for the user to type something, running the appropriate commands
        # to handle their actions.
        Duty.handle_input()

def add_rooms():
    """
    Adds all of the rooms to the game. 
    Duty.add_room() takes a string for the name of a room and a list of strings for the items in the room.
    """
    # Check if there's any command-line argument
    # If there is, then load room from text-file
    if len(sys.argv) > 1:
        
        room_list = load_room_from_file(sys.argv[1]) 
        for rooms in range(len(room_list)):
            Duty.add_room(room_list[rooms][0], room_list[rooms][1])
        
    # If there is none, load the default
    else: 
        Duty.add_room("Living Room", ["42\" TV Playing Golf", "Black Leather Sofa", "Circular Metal Coffee Table", "Wooden Bookshelf with 3 Shelves"])
        Duty.add_room("Kitchen", ["Gas Stove", "Retro Red Metal Refrigerator", "Oak Wooden Table", "4 Wooden Chairs"])
        Duty.add_room("Bedroom", ["Queen Size Bed", "Oak Wooden Nightstand", "Oak Wooden Dresser", "Oak Wooden Desk", "Oak Wooden Chair", "99 Red Balloons"])
        Duty.add_room("Bathroom", ["Toilet with Oak Seat", "Chrome Sink", "Shower with Blue Tiles", "Medicine Cabinet", "12 oz Shampoo"])
            
def load_room_from_file(file_name: str) -> list:
        
        """
        Load rooms from the file through this writing convention:
        
        room name-item 1, item 2, item 3,
        
        We will have a two-dimensional list after this process (like the default Duty.add_room convention)
        """
        file_handle = open(file_name, "r")
        room_list = []
              
        # iterate through all the lines
        # Remove the "-" and "\n"
        # And append it in our list
        # Note: We will have a two-dimensional list
        for rooms in file_handle.readlines():
            room_list.append(rooms.rstrip('\n').split("-"))
        
        # iterate through lenght of our room_list
        # Remove all "," for all the items
        # Note: room names are at [0], while items are at [1]
        for item_lists in range(len(room_list)): 
            x = room_list[item_lists][1].split(",")
            room_list[item_lists][1] = x
              
        return room_list
         
def register_anomalies():
    """
    Each anomaly we want to add to the game must be "Registered". 
    This is so the game knows what anomalies are possible.
    They will all be stored in UPPERCASE to make it easier to compare them later.
    """
    #Duty.register_anomaly("CAMERA MALFUNCTION")
    Duty.register_anomaly("NUMBER DISTORTION")
    #Duty.register_anomaly("MISSING ITEM")
    #Duty.register_anomaly("ITEM MOVEMENT")

def create_anomaly() -> bool:
    """f
    This little helper function handles the control flow for three steps:
    1. Choose a random room that does not have an anomaly, because rooms can only have one anomaly.
    2. Choose a random anomaly from the list of registered anomalies.
    3. Create the anomaly in the room.

    Return True if an anomaly was created, False if no anomaly was created.
    """

    # Choose a random room that does not have an anomaly
    room = Duty.get_random_unchanged_room()

    # Pick a random anomaly from the list of registered anomalies
    # Note: It is possible that some anomalies you create can't work in every room.
    # Maybe you will need additional logic to make sure the anomaly makes sense in the room.
    anomaly = Duty.get_random_anomaly()

    # Camera Malfunction is actually a special one.
    # It will not show this camera when clicking through if 
    # It sees CAMERA MALFUNCTION as the anomaly name
    if anomaly == "CAMERA MALFUNCTION":
        # All anomalies are stores as all uppercase
        # Since a camera malfunction means no items are shown, we pass an empty list
        return Duty.add_anomaly("CAMERA MALFUNCTION", room, [])
    elif anomaly == "NUMBER DISTORTION":
        return number_distortion(room)
    elif anomaly == "MISSING ITEM":
        # We pass the name of the room to these functions to separate out the logic
        return missing_item(room)
    elif anomaly == "ITEM MOVEMENT":
        return item_movement(room)
    else:
        print(f"ERROR: Anomaly {anomaly} not found")
        return False

def number_distortion(room: str) -> bool:
    """
    Pick random item from the room, and either increase or decrease that number by 1.
    This function will call change_number()
    
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Make a copy of items to avoid accidentally modifying the original item list
    3. Find a random item inside a room that has number/digit in it (any(chr.isdigit() for chr in new_items[random_item]))
    4. If it found one (randomly), we will change that item using change_number()
    5. Plug that changed item in our item list
    6. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """
    items = Duty.get_room_items(room)
    new_items = items[:]
    
    while True:
        # Find a random item inside room
        random_item = random.randint(0, len(new_items) - 1)
        
        # This value will become True if it founds any number/digit in the selected item
        # Otherwise, it will be False
        there_is_number = any(chr.isdigit() for chr in new_items[random_item])
        
        if there_is_number:
            new_items[random_item] = change_number(new_items[random_item])
            break
            
    # add_anomaly returns True if the anomaly was created, False if it was not.
    return Duty.add_anomaly("NUMBER DISTORTION", room, new_items)
        
def change_number(any_string: str) -> str:
    """
    Change the number(s) in a given string. Either increase/decrease it by 1.
    After the change, the data type will be a string again.
    
    1. Initialize an empty string
    2. Scan through all the characters in that string
    3. If it found any digit, 
        a. Convert that character into integer
        b. Add/Subtract 1
        b. Store it in a variable as a string
    4. Add that character into the empty string, along with other unchanged characters.
    5. Return the new/changed string
    """
    new_string = ""
    
    randomizer = random.randint(0, 1)
        
    for i, char in enumerate(any_string):
        if char.isdigit():
            x = int(char)
            if randomizer == 0:
                x += 1
            else:
                x -= 1
            new_string += str(x)
        else:
            new_string += any_string[i]
         
    return new_string

def missing_item(room: str) -> bool:
    """
    Removes a random item from the room. This is a pretty straightforward one.
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Choose a random item to remove. (random.randint())
    3. Make a copy of the list of items and remove the item from the copy. (list slicing)
    4. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """
    items = Duty.get_room_items(room)
    item_index_to_remove = random.randint(0, len(items)-1)
    new_items = items[:]
    new_items.pop(item_index_to_remove)
    
    # add_anomaly returns True if the anomaly was created, False if it was not.
    return Duty.add_anomaly("MISSING ITEM", room, new_items)

def item_movement(room: str) -> bool:
    """
    Re-arranges two items in a room. This one is a little more complicated.
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Choose two random items to swap. (random.randint())
    3. Make a copy of the list of items and swap the two items. (list slicing)
    4. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """

    items = Duty.get_room_items(room)

    # If there is only one item in the room, we can't move anything!
    if len(items) < 2:
        return False

    # Find two random items to swap
    item_to_move = random.randint(0, len(items)-1)
    item_to_move_to = random.randint(0, len(items)-1)

    # Make sure the two items are not the same
    while item_to_move == item_to_move_to:
        item_to_move_to = random.randint(0, len(items)-1)

    # Make a copy to avoid accidentally modifying the original item list
    new_items = items[:]

    # The below swap is also possible with the line: new_items[item_to_move], new_items[item_to_move_to] = new_items[item_to_move_to], new_items[item_to_move]
    item_a = new_items[item_to_move]
    item_b = new_items[item_to_move_to]
    new_items[item_to_move] = item_b
    new_items[item_to_move_to] = item_a

    return Duty.add_anomaly("ITEM MOVEMENT", room, new_items)

main()
