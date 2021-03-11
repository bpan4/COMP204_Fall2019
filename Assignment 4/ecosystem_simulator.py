# Belle Pan
# 260839939

import random
import matplotlib.pyplot as plt


class Animal:
    
    # Initializer method
    def __init__(self, my_species):
        """
        Args:
           self: the object being created
           my_species: String describing the species name
        Returns:
           Nothing
        Behavior:
           Initializes a new animal, setting species to my_species
        """            
        self.species = my_species
        self.age = 0
        self.time_since_last_meal = 0
        self.has_moved = False

    def __str__(self):
        """
        Args:
           self: the object on which the method is called
        Returns:
           String summarizing the object
        """
        s= self.species+":, age="+str(self.age)+ \
            ", time_since_last_meal="+ \
            str(self.time_since_last_meal)+ \
            ", has_moved = "+str(self.has_moved)
        return s
    
    def can_eat(self, other):
        """
        Args:
           self: the object on which the method is called
           other: an object of type Animal
        Returns:
           True if self can eat other, and False otherwise...
        """         
        # WRITE YOUR CODE FOR QUESTION 3 HERE
        
        if self.species == "Lion" and other.species == "Zebra":
            return True
            #only lions can eat zebras, thus only this combination should return True
        return False
        

    def time_passes(self):
        """
        Args:
           self: the object on which the method is called
        Returns:
           Nothing
        Behavior:
           Increments age and time_since_last_meal
        """           
        # WRITE YOUR CODE FOR QUESTION 4 HERE
        
        self.age += 1
        self.time_since_last_meal += 1
        

    def dies_of_old_age(self):
        """
        Args:
           self: the object on which the method is called
        Returns:
           True if animal dies of old age, False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 5 HERE
    
        if self.species == "Lion":
            if self.age == 18: 
                return True
        if self.species == "Zebra":
            if self.age == 7:
                return True
        return False
            

    def dies_of_hunger(self):
        """
        Args:
           self: the object on which the method is called
        Returns:
           True if animal dies of hunger, False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 6 HERE
        
        if self.species == "Lion":
            if self.time_since_last_meal == 6:
                return True
        return False
        
    def will_reproduce(self):
        """
        Args:
           self: the object on which the method is called
        Returns:
           True if ready to reproduce, False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 7 HERE
        
        if self.species == "Lion":
            if self.age == 7 or self.age == 14: 
                return True
                #lions only reproduce at age 7 and 14 months
        if self.species == "Zebra":
            if self.age == 3 or self.age == 6:
                return True
                #zebras only reproduce at age 3 and 6 months
        return False

    # end of Animal class



# DO NOT CHANGE THIS FUNCTION
def initialize_grid(size):
    """
    Args:
       size: The size of the grid to be created
    Returns:
       The grid, with some animals placed into it
    """    
    grid=[]
    # Create a size x size grid with all cells initialized to None
    for row in range(size):
        grid.append([])
        for col in range(size):
            grid[row].append(None)

    # place some animals in the grid. 
    # This will be the initial state of our simulation
    grid[3][5]=Animal("Lion")
    grid[7][4]=Animal("Lion")
    grid[2][1]=Animal("Zebra")
    grid[5][8]=Animal("Zebra")
    grid[9][2]=Animal("Zebra")
    grid[4][4]=Animal("Zebra")
    grid[4][8]=Animal("Zebra")
    grid[1][2]=Animal("Zebra")
    grid[9][4]=Animal("Zebra")
    grid[1][8]=Animal("Zebra")
    grid[5][2]=Animal("Zebra")
    return grid


# Use this function to print a grid; useful for debugging!
def print_grid(grid):
    """
    Args:
       grid: The grid to be printed
    Returns:
       Nothing
    Behavior:
       Prints the grid
    """  
    print("*"*(len(grid)+2))
    for i,row in enumerate(grid):
        print("*",end="")
        for cell in row:
            if cell!=None:
                print(cell.species[0],end="")
            else:
                print(" ",end="")
        print("*")
    print("*"*(len(grid)+2))


def my_random_choice(choices):
    """
    Args:
       choices: list of tuples
    Returns:
       One of tuples in the list
    """
    if not choices:
        return None
    
    # for debugging purposes
    def getKey(x):
        return x[0]+0.1*x[1]
    return min(choices, key=getKey)    

    # for actual random selection, uncomment this:
    #return random.choice(choices)


def list_neighbors(current_row, current_col, grid):
    """
    Args:
       current_row: Current row of the animal
       current_col: Current column of the animal
       grid: The grid
    Returns:
       List of all position tuples that are around the current position,
       without including positions outside the grid
    """
  
    # WRITE YOUR CODE FOR QUESTION 1 HERE
    
    all_positions = []
    #creates empty list to store possible positions
    rows = [current_row]
    cols = [current_col]
    #creates lists to store possible rows and columns, already includes current row and column
    for row in range(len(grid)):
        if row-current_row == 1:
            rows.append(row)
        if row-current_row == -1:
            rows.append(row)
    #iterates through rows in the grid, if the row is larger or smaller than the current row by 1, the index of the row is added to the list of rows
    for col in range(len(grid[0])):
        if col-current_col == 1:
            cols.append(col)
        if col-current_col == -1:
            cols.append(col)
        #iterates through columns in the grid, if the column is larger or smaller than the current column by 1, the index of the row is added to the list of columns
    for row in rows:
        for col in cols:
            all_positions.append((row,col))
    #iterates through all values in both rows and cols list and appends all possible tuples to the all_positions list
    all_positions.remove((current_row,current_col))
    #removes the current position from the generated list
    all_positions.sort()
    #sorts the list of tuples by their first integer
    return all_positions


            
def random_neighbor(current_row, current_col,animal_grid, only_empty=False):
    """
    Args:
       current_row: Current row of the animal
       current_col: Current column of the animal
       size: Size of the grid
       only_empty: keyword argument. If True, we only consider neighbors where 
                   there is not already an animal
    Returns:
       A randomly chosen neighbor position tuple

    SPECIAL ADVICE: YOU MAY BE TEMPTED TO DO THIS BY ITERATING OVER ELEMENTS
    OF A LIST OF POSITIONS AND REMOVING THOSE THAT ARE NOT EMPTY. 
    THAT WOULD BE A BAD THING TO DO; MODIFYING THE CONTENT OF A LIST ONE IS 
    CURRENTLY ITERATING OVER LEADS TO ALL KINDS OF UNEXPECTED BEHAVIORS.
    """
    
    # WRITE YOUR CODE FOR QUESTION 2 HERE
    
    all_positions = list_neighbors(current_row, current_col, animal_grid)
    empty = []
    if only_empty == True:
        for position in all_positions:
            if animal_grid[position[0]][position[1]] == None:
                empty.append(position)
                #only keeps track of locations that are empty around the animal
        if len(empty) == 0:
            return None
        return my_random_choice(empty)
    else:
        return my_random_choice(all_positions)
                


def one_step(animal_grid):
    """
    Args:
       animal_grid: The current state of the simulation
    Returns:
       List of strings describing the events that took place
    Behavior:
       Updates the content of animal_grid by simulating one time step
    """      
    # WRITE YOUR CODE FOR QUESTION 8 HERE
    
    events = []
    #keeps track of the events that occur at each iteration
    
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None:
                animal_grid[row][col].has_moved = False
                #Resets the has_moved attribute to False for all animals in the grid
                
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None:
                animal_grid[row][col].time_passes()
                #all animals age by 1 month and have not eaten for 1 month
                
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None:
                if animal_grid[row][col].dies_of_old_age() == True:
                    events.append((str(animal_grid[row][col].species) + " dies of old age at position " + str(row) + " " + str(col)))
                    animal_grid[row][col] = None
                    #removes all animals that have exceeded their lifespan (age) from the simulation
                    
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None:
                if animal_grid[row][col].dies_of_hunger() == True:
                    events.append((str(animal_grid[row][col].species) + " dies from hunger at position " + str(row) + " " + str(col)))
                    animal_grid[row][col] = None
                    #removes all animals that have starbed from the simulation
                    
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None and animal_grid[row][col].has_moved == False:
            #only moves an animal if it is present in the current row,col and has not already moved
                new_spot = random_neighbor(row, col, animal_grid)
                if animal_grid[new_spot[0]][new_spot[1]] != None:
                #if the location the animal is moved to is already occupied by another animal
                    if animal_grid[row][col].can_eat(animal_grid[new_spot[0]][new_spot[1]]):
                        animal_grid[row][col].has_moved = True
                        #updates the has_moved attribute to True
                        animal_grid[new_spot[0]][new_spot[1]] = animal_grid[row][col]
                        animal_grid[new_spot[0]][new_spot[1]].time_since_last_meal = 0
                        #updates the time_since_last_meal attribute of the animal that is moving
                        animal_grid[row][col] = None
                        events.append(("Lion moves from " + str(row) + " " + str(col) + " to " + str(new_spot[0]) + " " + str(new_spot[1]) + " and eats Zebra"))
                        #if the animal that is moving can consume the animal in the new location, it replaces the animal in the new location and the event is appended to the list of events that happen during this month
                    elif animal_grid[new_spot[0]][new_spot[1]].can_eat(animal_grid[row][col]):
                        animal_grid[new_spot[0]][new_spot[1]].time_since_last_meal = 0
                        #updates the time_since_last_meal attribute of the animal in the new location
                        animal_grid[row][col] = None
                        events.append(("Zebra moves from " + str(row) + " " + str(col) + " to " + str(new_spot[0]) + " " + str(new_spot[1]) + " and is eaten by Lion"))
                        #if the animal that is moving can be consumed the animal in the new location, it is removed and the event is appended to the list of events that happened during the month
                elif animal_grid[new_spot[0]][new_spot[1]] == None:
                    animal_grid[row][col].has_moved = True
                    #updates the has_moved attribute to True
                    animal_grid[new_spot[0]][new_spot[1]] = animal_grid[row][col]
                    animal_grid[row][col] = None
                    events.append((str(animal_grid[new_spot[0]][new_spot[1]].species) + " moves from " + str(row) + " " + str(col) + " to empty " + str(new_spot[0]) + " " + str(new_spot[1])))
                    #the movement of an animal to an empty space is appended to the list of events that happened during the month
                elif animal_grid[new_spot[0]][new_spot[1]] == animal_grid[row][col]:
                    animal_grid[row][col].has_moved = True
                    #if the animal is moving into a space that is already holding an animal that is identical to it, it cannot move
                    
    for row in range(len(animal_grid)):
        for col in range(len(animal_grid[0])):
            if animal_grid[row][col] != None:
                if animal_grid[row][col].will_reproduce() == True:
                    birth_spot = random_neighbor(row, col,animal_grid, only_empty=True)
                    #generates a random locations to place the baby animal, must be an empty location or it would return None
                    if birth_spot != None:
                        animal_grid[birth_spot[0]][birth_spot[1]] = Animal(animal_grid[row][col].species)
                        #places the new animal at the location IF the location specified is NOT None
                        events.append(("Birth of a " + str(animal_grid[row][col].species) + " at " + str(birth_spot[0]) + " " + str(birth_spot[1])))
                        #the birth of an animal is appended to the list of events that happened during the month
    return events
                    
                    
                    
                
                    

      

def run_whole_simulation(land_size = 10, simulation_duration = 20, image_file_name="population.png"):
    """
    Args:
       land_size: Size of the grid
       simulation_duration: Number of steps of the simulation
       image_file_name: name of image to be created.
    Returns:
       Nothing
    Behavior:
       Simulates the evolution of an animal grid
       Generates graph of species abundance and saves it to populations.png
    """      
    # Do not change this; this initializes the grid
    animal_grid = initialize_grid(land_size)

    # WRITE YOUR CODE FOR QUESTION 9 HERE
    
    plt.ylabel = "Number of Individuals"
    plt.xlabel = "Time"
    zebra_counter = []
    lion_counter = []
    
    for time in range(simulation_duration):
        zebra = 0
        lion = 0
        one_step(animal_grid)
        for row in range(len(animal_grid)):
            for col in range(len(animal_grid[0])):
                if animal_grid[row][col] != None:
                    if animal_grid[row][col].species == "Lion":
                        lion += 1
                    elif animal_grid[row][col].species == "Zebra":
                        zebra += 1
        zebra_counter.append(zebra)
        lion_counter.append (lion)
        #appends the number of zebras and lions at each iteration to their respective lists
        
    plt.plot (zebra_counter, 'r-', label = "Zebra")
    plt.plot (lion_counter, 'b-', label = "Lion")
    plt.legend()
    plt.savefig(image_file_name)
    
    


def my_test():
    land_size = 10
    animal_grid = initialize_grid(land_size)   
    
    print("Question 1")
    print("Neighbors of 5 5:",list_neighbors(5,5,animal_grid))
    print("Neighbors of 9 5:",list_neighbors(9,5,animal_grid))      
    print("Neighbors of 0 0:",list_neighbors(0,0,animal_grid))      
    print("Neighbors of 9 0:",list_neighbors(9,0,animal_grid))      

    print("Question 2")
    print("Random neighbor of 5 5, only empty:",random_neighbor(5, 5,animal_grid, only_empty=True))
    print("Random neighbor of 5 5:",random_neighbor(5, 5,animal_grid))
    print("Random neighbor of 9 5:",random_neighbor(9, 5,animal_grid))
    print("Random neighbor of 0 0:",random_neighbor(0, 0,animal_grid))
    print("Random neighbor of 9 0:",random_neighbor(9, 0,animal_grid))

    print("Question 3")
    a = Animal("Lion")
    b = Animal("Zebra")
    print("Lion can eat Zebra?",a.can_eat(b))
    print("Zebra can eat Lion?",b.can_eat(a))
    print("Lion can eat Lion?",a.can_eat(a))
#    
    print("Question 4-7")
    a.time_passes()
    print(a)
    b.time_passes()
    print(b)
    b.time_passes()
    print(b)
#    
    print("Question 5 and 6")
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    a.time_passes()
    b.time_passes()
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    a.time_passes()
    b.time_passes()
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    a.time_passes()
    b.time_passes()
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    a.time_passes()
    b.time_passes()
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    a.time_passes()
    b.time_passes()
    print("Zebra dies of old age?",b.dies_of_old_age())
    print("Lion dies of hunger?",a.dies_of_hunger())
    print("Zebra will reproduce?",b.will_reproduce())
    
    print("Question 8")

    animal_grid = initialize_grid(10)
    for time in range(20):
        print("Time ",time)
        print_grid(animal_grid)
        events=one_step(animal_grid)
        print("Events = ",events)
#    
    print("Question 9")
    run_whole_simulation()
#    

# DO NOT CHANGE; IT ALLOWS US TO IMPORT YOUR CODE WITHOUT HAVING TO EDIT IT
if __name__ == "__main__":
    my_test()
    