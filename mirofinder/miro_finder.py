def get_maze_answer(maze : dict) -> list:
    
    solution = []
    now_location = max(maze.keys())
    movement_step = 0

    direction = []
    reversed_direction = {"E":"W", "W":"E", "N":"S", "S":"N", "":""}

    while True:
        movement_list = maze.get(now_location)
        movement = [{"direction": "E", "location": (now_location[0], now_location[1] + 1)}, 
                    {"direction": "W", "location": (now_location[0], now_location[1] - 1)}, 
                    {"direction": "N", "location": (now_location[0] - 1, now_location[1])}, 
                    {"direction": "S", "location": (now_location[0] + 1, now_location[1])}]
        
        now_direction = movement[movement_step]["direction"]
        before_direction = direction[-1] if len(direction) > 0 else ""

        if (movement_list[now_direction]) & (now_direction != reversed_direction[before_direction]): 
            solution.append(now_location) 
            direction.append(now_direction)
            now_location = movement[movement_step]["location"] 
            before_direction = now_direction 
            movement_step = 0 

        else:
            if movement_step < 3: 
                movement_step += 1
            else: 
                now_location = solution.pop()
                before_direction = direction.pop()
                movement_step = list(reversed_direction.keys()).index(before_direction) + 1


        if now_location == (1, 1):
            solution.append(now_location)
            print("solution : ", solution)
            break
        
    return solution

if __name__ == "__main__":
    get_maze_answer({(1, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (2, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (3, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (1, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (2, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (3, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 0},
                (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (2, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (3, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}})