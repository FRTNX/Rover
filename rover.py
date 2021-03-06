# Rover simulator

def init():
    current_pos, grid_boundaries, direction, commands = get_commands()
    run(current_pos, direction, grid_boundaries, commands)


def get_commands():
    """Parses command file and sends the extracted values
       to the main run() function
    """                                      
    commands_file = open('cmds', 'r')                                                     
    data = commands_file.read().split('\n')[:3]                                               
    commands_file.close()
    for i in range(len(data)):
        data[i] = data[i].rstrip()  # removes trailing whitespace from line in command file                                          
    print('got the following commands: %s' % data)                        
    raw_limits = data[0].split()
    x_limit = int(raw_limits[0])
    y_limit = int(raw_limits[1])    
    starting_point_raw = list(data[1].replace(' ', ''))
    x = int(starting_point_raw[0])       
    y = int(starting_point_raw[1])    
    direction = starting_point_raw[2]                                               
    commands = list(data[2])
    return (x, y), (x_limit, y_limit), direction, commands


def run(current_pos, direction, boundary, commands):
    """Takes in parsed commands and iterates through them to return rovers final location
       on the grid after all commands have been executed. 

       params:
           current_pos -> tuple : the Cartesian coordinates of the rovers current position.
           direction   -> string: a letter denoting the current direction of the rover. Valid 
                                  values are N, W, E, and S (which represent North, West, East,
                                  and South, respectively)
           boundary    -> tuple : Cartesian points of the grid boundary.
           commands    -> list  : The list of commands to be executed. Valid commands are M, L, 
                                  and R (representing Move-forward, turn-Left, and turn-Right,
                                  respectively)
    """
    print('pos: %s, direction: %s, boundary: %s, commands: %s' % (current_pos,
                                                                  direction,
                                                                  boundary,
                                                                  commands
    ))                        
    if commands == []:
        print('Rover completed running commands facing %s on grid point %s' % (get_direction_name(direction),
                                                                               current_pos))          
        return current_pos          
    else:                                
        command = commands[0]
        if command == "M":
            current_pos = move_forward(current_pos, direction, boundary)
            if current_pos == 'Out of bounds':
                print('Rover has moved out of surveyed grid area.')
                exit()
        else:             
            direction = shift(direction+command)        
        commands.pop(0)
        run(current_pos, direction, boundary, commands)


def move_forward(current_pos, current_direction, limits):
    """Moves the Rover one block forward                                       
                                                                            
       params:                                                             
           current_pos -> tuple: contains the current Cartesian position of the Rover.
    """                       
    x, y = current_pos          
    directions = {                  
                  "N": (0, 1),           
                  "S": (0, -1),
                  "E": (1, 0),
                  "W": (-1, 0)                                          
                 }        
    x += directions[current_direction][0]               
    y += directions[current_direction][1]
    if not out_of_bounds(x, y, limits[0], limits[1]):  
        return (x, y)
    else:   
        return 'Out of bounds'


def out_of_bounds(x, y, x_limit, y_limit):
    """Checks whether the rover has moved out of surveyed grid.

       params:
           x       -> int: x coordinate
           y       -> int: y coordinate
           x_limit -> int: furthest allowed value of x from origin
           y_limit -> int: furthest allowed value of y from origin
    """               
    if (x <= x_limit and x >= 0) and (y <= y_limit and y >= 0):                                         
        return False                                                        
    else:                                                                  
        return True  


def shift(key):
    """Maps current direction acted on by either L or R command to new direction
       
       params:
           key -> string: a string composed of the concatenation of the rovers current direction
                          and the direction in which it should turn 90 degrees to.
    """                                          
    mapper = {                                                                
              "NL": "W",                                                    
              "NR": "E",                                                   
              "SL": "E",                                                              
              "SR": "W",      
              "EL": "N",        
              "ER": "S",            
              "WL": "S",                 
              "WR": "N"        
             }                
    return mapper[key]


def get_direction_name(initial):
    directions = {
                  "N": "North",
                  "S": "South",
                  "W": "West",
                  "E": "East"
                 }
    return directions[initial]


if __name__ == '__main__':
	init()