

# Python Game: "I Am On Duty Watching Changes to Rooms"

## Overview
This is a text-based Python game where you play as a security guard monitoring rooms for anomalies. Your goal is to detect and report any changes or anomalies in the rooms before too many anomalies accumulate, which will result in losing the game. The game runs in real-time, with in-game time passing faster than real-time based on the timescale setting.

---

## How to Play
1. **Monitor Rooms**: Use the cameras to observe the rooms and their items.
2. **Detect Anomalies**: Look for changes in the items within the rooms. Anomalies can include:
   - **Number Distortion**: Numbers in item descriptions may increase or decrease.
   - **Missing Item**: An item may disappear from a room.
   - **Item Movement**: Items may swap places within a room.
3. **Report Anomalies**: When you notice an anomaly, report it by selecting the correct room and anomaly type.
4. **Avoid Too Many Anomalies**: If too many anomalies accumulate (default: 4), you lose the game.
5. **Complete Your Shift**: Survive until the end of your shift (default: 5 in-game hours) to win.

---

## Game Commands
- **Next Camera** (`n` or `enter`): Move to the next camera.
- **Previous Camera** (`p`): Move to the previous camera.
- **Report Anomaly** (`r`): Report an anomaly in a room.
- **Quit Game** (`q`): Quit the game.
- **Help** (`h` or `?`): Display the list of commands.

---

## Setup and Running the Game

### Prerequisites
- Python 3.x installed on your system.
- No additional libraries are required.

### Running the Game
1. Save the provided Python code in a file named `RunGame_696_726.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the game using the command:
   ```bash
   python RunGame_696_726.py
   ```
5. Optionally, you can load rooms from a text file by passing the file name as a command-line argument:
   ```bash
   python RunGame_696_726.py rooms_with_items.txt
   ```

### Customizing Rooms
You can define rooms and their items in a text file (e.g., `rooms_with_items.txt`) using the following format:
```
Room Name-Item 1, Item 2, Item 3,
```

Example:
```
Living Room-42" TV Playing Golf, Black Leather Sofa, Circular Metal Coffee Table,
Kitchen-Gas Stove, Retro Red Metal Refrigerator, Oak Wooden Table,
```

---

## Game Settings
You can customize the game by modifying the following settings in the `main()` function:
- **Debug Mode**: Set to `True` to display additional debugging information.
- **Timescale**: Controls how fast in-game time passes relative to real-time (default: 60 seconds in-game per real second).
- **Probability**: The chance of an anomaly occurring per in-game minute (default: 0.1 or 10%).
- **Max Anomalies**: The maximum number of active anomalies allowed before losing the game (default: 4).
- **Min Seconds Between Anomalies**: The minimum time (in-game seconds) between anomalies (default: 10 minutes).

---

## Code Structure
- **`main()`**: The main function initializes the game and runs the game loop.
- **`add_rooms()`**: Adds rooms to the game, either from a file or using default values.
- **`register_anomalies()`**: Registers the types of anomalies that can occur in the game.
- **`create_anomaly()`**: Handles the creation of anomalies in the game.
- **`number_distortion()`**: Implements the "Number Distortion" anomaly.
- **`missing_item()`**: Implements the "Missing Item" anomaly.
- **`item_movement()`**: Implements the "Item Movement" anomaly.
- **`Duty.py`**: Contains the game logic and management (do not modify this file).

---

## Credits
This game was developed as a collaborative effort by:

- **Santo Mukiza**   
- **Jhernie Magnampo**   

### Contributions
- **Santo Mukiza**:
  - Collaborated on implementing file reading and parsing for loading rooms from a text file.
  - Researched and implemented string manipulation techniques to detect and modify numbers in item descriptions.
  - Contributed to the logic for creating and managing anomalies, including the "Number Distortion" anomaly.
  - Assisted in debugging and testing the game to ensure smooth functionality.

- **Jhernie Magnampo**:
  - Collaborated on implementing file reading and parsing for loading rooms from a text file.
  - Researched and implemented the use of `enumerate()` for iterating through lists and strings.
  - Contributed to the logic for creating and managing anomalies, including the "Missing Item" and "Item Movement" anomalies.
  - Assisted in debugging and testing the game to ensure smooth functionality.

---

## Pair Programming Approach
- **Collaboration**: We worked together in person at the library, ensuring constant communication and idea sharing.
- **Independent Work**: Both of us independently researched and implemented key features, such as file reading and string manipulation.
- **Role Switching**: We switched roles (driver and navigator) at least once during every meeting to ensure balanced contributions.
- **Future Improvements**: We found the pair programming process effective and do not plan to make significant changes to our approach in the future.

---

