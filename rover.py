# Rover simulator

def init():                                         
    f = open('cmds', 'r')                                                     
    ff = f.read().split('\n')                                               
    f.close()                                                              
    print('got the following commands: %s' % ff)                          
    raw_limits = ff[0].split()
    x_limit = int(raw_limits[0])
    y_limit = int(raw_limits[1])    
    sp_raw = list(ff[1].replace(' ', ''))
    x = int(sp_raw[0])       
    y = int(sp_raw[1])    
    direction = sp_raw[2]                                               
    commands = list(ff[2])
    run((x, y), direction, (x_limit, y_limit), commands)


def run(current_pos, direction, boundary, commands):
    print('pos: %s, direction: %s, boundary: %s, commands: %s' % (current_pos,
                                                                  direction,
                                                                  boundary,
                                                                  commands
    ))                        
    if commands == []:          
        return current_pos          
    else:                                
        command = commands[0]
        if command == "M":
            current_pos = move_forward(current_pos, direction, boundary)
        else:             
            direction = shift(direction+command)        
        commands.pop(0)
        run(current_pos, direction, boundary, commands)


def move_forward(current_pos, current_direction, limits):
    """Moves the Rover on block forward                                       
                                                                            
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
        print('Rover has moved out of grid boundary')
        exit()


def out_of_bounds(x, y, x_limit, y_limit):               
    if (x <= x_limit) and (y <= y_limit):                                         
        return False                                                        
    else:                                                                  
        return True  


def shift(key):                                          
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


if __name__ == '__main__':
	init()