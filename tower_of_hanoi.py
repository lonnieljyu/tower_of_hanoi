import random
import numpy

"""
tower_of_hanoi.py
- Lonnie Yu

Sets up a Tower of Hanoi game with the given input parameters.
Makes random valid moves for T iterations.
Calculates the center of mass at each iteration.
Returns the center of mass mean and standard deviation (std).
"""

# Returns of a set of move tuples (stack position, direction)
def Get_Move_Set(stacks):
    moves = set()
    M = len(stacks) # number of stacks
    
    print("Get Move Set")
    print(stacks)
    for i in range(M):
        # print("i:", i)
        # print(stacks[i])
        
        current_stack = stacks[i]
        if(current_stack):
        
            # Add left move if valid 
            if (i > 0 and (not stacks[i-1] 
                            or current_stack[-1] < stacks[i-1][-1])):
                moves.add((i, -1))
            
            # Add right movie if valid 
            if (i < M - 1 and (not stacks[i+1] 
                                or current_stack[-1] < stacks[i+1][-1])):
                moves.add((i, 1))
        
    return moves
    
# Returns new list of stacks with executed move
def Execute_Move(stacks, move):
    source_stack_index = move[0]
    destination_stack_index = move[0] + move[1]
    stacks[destination_stack_index].append(stacks[source_stack_index].pop())
    return stacks

def Run_Tower_Of_Hanoi(number_of_stacks, number_of_disks, number_of_iterations):
    # Initialize data structures
    stacks = [list() for i in range(number_of_stacks)]
    stacks[0] = [weight for weight in reversed(range(1, number_of_disks+1))]
    centers_of_mass = list()
    
    
    # Loop over T iterations
    for t in range(1, number_of_iterations+1):
        print("")
        print("T: ", t)
        
        moves = Get_Move_Set(stacks)
        print(moves)
        
        # Randomly choose move from move set
        move = random.choice(list(moves))
        print(move)
        
        stacks = Execute_Move(stacks, move)
        
        # Calculate and append center of mass to list
        
    # Return center of mass mean and std
    
    print(stacks)

# Main 
if __name__ == "__main__":
    # Run_Tower_Of_Hanoi(3, 3, 16)
    Run_Tower_Of_Hanoi(6, 6, 256)
    