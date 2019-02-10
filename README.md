# Mars Rover Code Challenge

### Installation

To install and run the rover, simply clone the repository

```git clone https://github.com/FRTNX/Rover```

then

```cd Rover```

```python3 rover.py```

### So Whats Going On?

The code simulates the movements of a rover over a grid with defined limits. Due to the transmission delay in communicating  with the rover on Mars, a list of commands is sent to the rover. The rover will execute these commands then return the coordinates of its new position.

The command file format is of the form:
```
8 10
12 E
MMLMRMMRRMML
```
The first line describes the size of the current grid. This zone's boundary is at the Cartesian coordinate (8, 10).

The second line describes the rovers initial position on the grid along with its direction. In this example the rover is facing east at point (1, 2).

The third and final line is the list of commands the rover is to execute where

    M : moves the rover forward in the direction it faces

    L : Turns the rover 90 degrees to the left from its current direction

    R : Turns the rover 90 degress to right from its current direction
    
These commands are located in a file called ```cmds```. The values may be changed as necessary while respecting the required format described above.

The program is designed to fast and lightweight. No libraries were used in its implementation, thus limiting dependencies to simeply having python 3.
Tests have been included to ensure the rover is grid aware, knowing when it is out of bounds. Tests have also been included to make sure the rover turns on its axis properly.
