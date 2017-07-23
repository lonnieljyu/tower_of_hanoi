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

def Run_Tower_Of_Hanoi(number_of_stacks, number_of_disks, number_of_iterations):
    # Initialize data structures
    stacks = [list() for i in range(number_of_stacks)]
    stacks[0] = [weight for weight in reversed(range(1, number_of_disks+1))]
    centers_of_mass = list()
    
    # Loop over T iterations
    for t in range(1, number_of_iterations+1):
    
        # Build move set
        
        # Randomly choose move from move set
        
        # Calculate and append center of mass to list
        
        print("T: ", t)
        
    # Return center of mass mean and std
    
    print(stacks)

# Main 
if __name__ == "__main__":
    Run_Tower_Of_Hanoi(3, 3, 16)
    