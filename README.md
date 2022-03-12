# HillClimbing and Simulated Annealing
Solving random 8-queens puzzles using Hill Climbing and Simulated Annealing algorithms.

## Psuedocode for Hill Climbing algorithm
function hillClimbing(problem) <br>
___ current = problem.INITIAL_STATE <br>
_____ loop<br>
_______ neighbor = highest-value successor of current<br>
_________ if (neighbor.VALUE<=current.VALUE) then<br>
___________ return current.STATE<br>
_______ current = neighbor<br>
     
## Psuedocode for Simulated Annealing algorithm
function SimulatedAnnealing(problem)<br>
____ current=initial state of problem<br>
____ t=1 //initialize time<br>
____ loop<br>
_______ T = coolDown(t) //converts time in Temp.<br>
_______ if T=0 then return current<br>
__________ next = random successor of current<br>
_______ δE = next.VALUE - current.VALUE<br>
_______ if δE>0 then current=next<br>
_______ else current=next with some prob (e ^(δE/T))<br>
_______ t=t+1<br>
