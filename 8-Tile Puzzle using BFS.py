#Import the necessary libraries
from time import time
from queue import Queue
#Creating a class Puzzle
class Puzzle:
 #Setting the goal state of 8-puzzle
 goal_state=[1,4,2,3,5,0,6,7,8]
 num_of_instances=0
 #constructor to initialize the class members
 #works like the default constructor
 def __init__(self,state,parent,action): # value passed in it is (self,0,none,none) second pass
([1,2,3,8,0,4,7,6,5],self,0)
 self.parent=parent #-> 0 -> self
 self.state=state #state is the current state of the board -> set 0 -> [1,2,3,8,0,4,7,6,5]
 self.action=action # -> 0 -> 0

 #action is the action that is used to generate the current state from the parent state
 #TODO: incrementing the number of instance by 1
 # We are incrementing the number of instance by 1 to keep track of the number of nodes
generated
 Puzzle.num_of_instances +=1 # -> 1 -> 2
 print("Current state: ",Puzzle.num_of_instances)
 print(self.state)


 #function used to display a state of 8-puzzle

 def __str__(self):
 # state tree such that 0-2 in first row, 3-5 in second row and 6-8 in third row

 return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9]) # divided the single
list into 3 rows and 3 columns


 #method to compare the current state with the goal state
 def goal_test(self):
 #TODO: include a condition to compare the current state with the goal state
 if self.state == Puzzle.goal_state:
 print()
 print("Goal state found and printed in reverse order: ")
 print( )

print(str(Puzzle.goal_state[0:3])+'\n'+str(Puzzle.goal_state[3:6])+'\n'+str(Puzzle.goal_state[6:9]))
 #Puzzle.goal_state
 return True
 else:
 return False

 #static method to find the legal action based on the current board position
 #static method can be called without creating an object and can be called using the class name
 @staticmethod
 # i and j are the row and column of the board
 def find_legal_actions(i,j):
 legal_action = ['U', 'D', 'L', 'R'] # these are the actions performed on the board
 if i == 0:
 # if row is 0 in board then up is disable
 legal_action.remove('U')
 elif i == 2:
 #TODO: down is disable
 legal_action.remove('D')
 if j == 0:
 #TODO: Left is disable
 legal_action.remove('L')

 elif j == 2:
 #TODO: Right is disable
 legal_action.remove('R')
 return legal_action
 #method to generate the child of the current state of the board
 def generate_child(self):
 #TODO: create an empty list
 children=[] #empty list created
 x = self.state.index(0) #index(0) returns the row and column of the board -> 7

 # the value 0 in the board is the empty space
 # x is the index of the empty space in the board its stores the row and column of the board
in a single variable by using the formula x = i*3 + j
 i = int(x / 3) # divided by 3 to get the row of the board -> 2
 j = int(x % 3) # mod 3 to get the column of the board -> 1
 #example if x=4 then i=1 and j=1
 #TODO: call the method to find the legal actions based on i and j values
 legal_actions= Puzzle.find_legal_actions(i,j) #(2,1) passed to find_legal_action
 #legal_action = ['U', 'L', 'R']
 #TODO:Iterate over all legal actions
 for action in legal_actions:
 new_state = self.state.copy() #coping the current state of the board to new_state
 #if the legal action is UP

 if action == 'U':
 #Swapping between current index of 0 with its up element on the board
 # It is going to take the value of the element above the 0 that is 6 in the first step and
swap it with the 0
 new_state[x], new_state[x-3] = new_state[x-3], new_state[x]

 elif action == 'D':
 #TODO: Swapping between current index of 0 with its down element on the board
 new_state[x], new_state[x+3] = new_state[x+3], new_state[x]

 elif action == 'L':
 #TODO: Swapping between the current index of 0 with its left element on the board
 new_state[x], new_state[x-1] = new_state[x-1], new_state[x]

 elif action == 'R':
 #TODO: Swapping between the current index of 0 with its right element on the board
 new_state[x], new_state[x+1] = new_state[x+1], new_state[x]

 children.append(Puzzle(new_state,self,action))

 #TODO: return the children
 return children
 #method to find the solution
 def find_solution(self):
 solution = []
 solution.append(self.action)
 path = self
 while path.parent != None:
 path = path.parent

 print(" | ")
 print(path)

 solution.append(path.action)
 solution = solution[:-1]
 solution.reverse()
 return solution
#method for breadth first search
#TODO: pass the initial_state as parameter to the breadth_first_search method
def breadth_first_search(initial_state):
 start_node = Puzzle(initial_state,None,None) # call the class puzzle default constructor with
pass (0,none,none) as parameter
 print("Initial state:")
 print(start_node) # # in form of 3 lists -> call the __str__ method of puzzle class
 print()
 print("STATES OF THE BOARD ")
 if start_node.goal_test(): # check if goal state == initial state
 return start_node.find_solution()
 q = Queue() # created a queue object
 #TODO: put start_node into the Queue
 q.put(start_node) # startnode is the string having 3 lists in it ... so putting that string into the
queue
 #TODO: create an empty list of explored nodes
 explored=[]
 #TODO: Iterate the queue until empty. Use the empty() method of Queue
 while not(q.empty()): # currently as the queue is not empty so it will go inside the loop
 #TODO: get the current node of a queue. Use the get() method of Queue
 node= q.get()

 #TODO: Append the state of node in the explored list as node.state
 explored.append(node.state)
 #TODO: call the generate_child method to generate the child nodes of current node
 children= node.generate_child()
 #Jump to the generate_child method of Puzzle class
 #TODO: Iterate over each child node in children
 for child in children:
 if child.state not in explored:
 if child.goal_test():

 return child.find_solution()
 q.put(child)

 return
#Start executing the 8-puzzle with setting up the initial state
#Here we have considered 3 initial state intitalized using state variable
state=[[1, 2, 5,
 3, 4, 0,
 6, 7, 8]]
#Iterate over number of initial_state
for i in range(len(state)):
 #TODO: Initialize the num_of_instances to zero
 Puzzle.num_of_instances=0
 #Set t0 to current time
 t0=time()

 bfs=breadth_first_search(state[i]) # state[i] is at the first run is 0
 #Get the time t1 after executing the breadth_first_search method
 t1=time()-t0
 print()
 print('BFS:', bfs)

 print('space:',Puzzle.num_of_instances)
 print()
 print('time:',t1)
 print()
print('------------------------------------------')
