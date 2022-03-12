# HillClimbing and Simulated Annealing
Solving random 8-queens puzzles using Hill Climbing and Simulated Annealing algorithms.

## Psuedocode for Hill Climbing algorithm
function hillClimbing(problem) <br>
    current = problem.INITIAL_STATE <br>
    loop<br>
       neighbor = highest-value successor of current<br>
       if (neighbor.VALUE<=current.VALUE) then<br>
          return current.STATE<br>
       current = neighbor<br>
     
## Psuedocode for Simulated Annealing algorithm
function SimulatedAnnealing(problem)<br>
    current=initial state of problem<br>
    t=1 //initialize time<br>
    loop<br>
       T = coolDown(t) //converts time in Temp.<br>
       if T=0 then return current<br>
          next = random successor of current<br>
       δE = next.VALUE - current.VALUE<br>
       if δE>0 then current=next<br>
       else current=next with some prob (e ^(δE/T))<br>
       t=t+1<br>
