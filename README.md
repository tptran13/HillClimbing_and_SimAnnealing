# HillClimbing and Simulated Annealing
Solving random 8-queens puzzles using Hill Climbing and Simulated Annealing algorithms.

## Psuedocode for Hill Climbing algorithm
function hillClimbing(problem)
    current = problem.INITIAL_STATE
    loop
       neighbor = highest-value successor of current
       if (neighbor.VALUE<=current.VALUE) then
          return current.STATE
       current = neighbor
     
## Psuedocode for Simulated Annealing algorithm
function SimulatedAnnealing(problem)
    current=initial state of problem
    t=1 //initialize time
    loop
       T = coolDown(t) //converts time in Temp.
       if T=0 then return current
          next = random successor of current
       δE = next.VALUE - current.VALUE
       if δE>0 then current=next
       else current=next with some prob (e ^(δE/T))
       t=t+1
