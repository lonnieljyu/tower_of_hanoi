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

def Initialize_Stacks(number_of_stacks, number_of_disks):
    stacks = [list() for i in range(number_of_stacks)]
    stacks[0] = [weight for weight in reversed(range(1, number_of_disks+1))]
    return stacks
    
def IsLeftMoveValid(i, stacks):
    return ((i > 0) 
            and (not stacks[i-1] or stacks[i][-1] < stacks[i-1][-1]))
    
def IsRightMoveValid(i, stacks):
    return ((i < len(stacks) - 1) 
            and (not stacks[i+1] or stacks[i][-1] < stacks[i+1][-1]))
    
# Returns a set of move tuples (stack position, direction)
def Get_Move_Set(stacks):
    moves = set()   
    for i in range(len(stacks)):
        if(stacks[i]):
            if IsLeftMoveValid(i, stacks): moves.add((i, -1))
            if IsRightMoveValid(i, stacks): moves.add((i, 1))
    return moves
    
def Get_Random_Move(moves):
    return random.choice(list(moves))
    
# Returns new stacks list with executed move
def Execute_Move(stacks, move):
    source_stack_index = move[0]
    destination_stack_index = move[0] + move[1]
    stacks[destination_stack_index].append(stacks[source_stack_index].pop())
    return stacks
    
def Get_Sum_Of_Weigths(stacks):
    return numpy.array(numpy.array(stacks).sum()).sum()
    
def Get_Sum_Of_Weights_And_Position_Products(stacks):
    products = ((position * numpy.array(stack)).sum() for stack, position in zip(stacks, range(len(stacks))))
    return sum(products)
    
# Center of mass = sum(disk weight * stack position of disk) / sum(disk weight)
def Get_Center_Of_Mass(stacks):
    return Get_Sum_Of_Weights_And_Position_Products(stacks) / Get_Sum_Of_Weigths(stacks)
    
# Print Centers of Mass mean and std with 10-digit precision
def Print_Centers_Of_Mass_Statistics(centers_of_mass):
    array = numpy.array(centers_of_mass)
    mean = array.mean()
    std = array.std(ddof=0)
    print("mean:", mean)
    print("std:", std)
    
def Run_Tower_Of_Hanoi(number_of_stacks, number_of_disks, number_of_iterations):
    stacks = Initialize_Stacks(number_of_stacks, number_of_disks)
    centers_of_mass = list()
    print(stacks)
    
    for t in range(1, number_of_iterations+1):
        print("\nT: ", t)
        
        moves = Get_Move_Set(stacks)
        print(moves)
        
        move = Get_Random_Move(moves)
        print(move)
        
        stacks = Execute_Move(stacks, move)
        print(stacks)
        
        center_of_mass = Get_Center_Of_Mass(stacks)
        print(center_of_mass)
        
        centers_of_mass.append(center_of_mass)
    
    print("\nFinal stacks:")
    print(stacks)    
    
    Print_Centers_Of_Mass_Statistics(centers_of_mass)

# Main 
if __name__ == "__main__":
    Run_Tower_Of_Hanoi(3, 3, 16)
    # Run_Tower_Of_Hanoi(6, 6, 256)
    