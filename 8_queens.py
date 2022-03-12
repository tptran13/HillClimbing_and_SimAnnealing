import sys
import random
import math
from math import exp as e

def board (num_of_puzzles):       
    total_hc_cost = 0
    total_sa_cost = 0
    total_hc_solved = 0
    total_sa_solved = 0

    b = 1
    while b <= num_of_puzzles:
        initial_state = gen_board()     #initial state
        hc_cost, hc_solved = hill_climbing(initial_state)       #solve hill climbing
        total_hc_cost += hc_cost
        total_hc_solved += hc_solved
        sa_cost, sa_solved = sim_annealing(initial_state)       #solve simulated annealing
        total_sa_cost += sa_cost
        total_sa_solved += sa_solved
        b += 1

    return solve(total_hc_solved, num_of_puzzles), total_hc_cost, solve(total_sa_solved, num_of_puzzles), total_sa_cost

def hill_climbing(board):
    current = board.copy() 
    solved = 0
    cost = 0    
    while True:
        neighbor = get_best_successor(current)
        if num_of_attacks(neighbor) >= num_of_attacks(current):
            if num_of_attacks(current) == 0:
                solved += 1
            return cost, solved
        else:
            current = neighbor
            cost += 1

def sim_annealing(board):
    current = board.copy()
    solved = 0
    cost = 0    
    t = 1 #initialize time
    while True:
        T = coolDown(t) #converts time in Temp.
        if T == 0:
            if(num_of_attacks(current) == 0):
                solved += 1
            return cost, solved
        next = get_random_successor(current)
        E = num_of_attacks(next) - num_of_attacks(current)
        if E > 0:
            current = next
            cost += 1
        else:
            if random.random() > compute_prob(E, T):
                cost += 1
                current = next 
        t += 1

def get_best_successor(current):   
    min_heuristic = num_of_attacks(current)  
    best_successor = current
    for q in range(1, len(current)):
        for pos in range(1, len(current)):
            successor = move(q, pos, current)
            successor_heuristic = num_of_attacks(successor)     
            if successor_heuristic < min_heuristic:     
                min_heuristic = successor_heuristic
                best_successor = successor
    return best_successor

def get_random_successor(current):   #create a list of successors and randomly pick a successor
    successor_list = []
    min_heuristic = num_of_attacks(current)
    for q in range(1, len(current)):
        for pos in range(1, len(current)):
            successor = move(q, pos, current)
            successor_heuristic = num_of_attacks(successor)  
            if successor_heuristic <= min_heuristic:    #decrease list's size by appending the state with the minimal number of attacking queens
                successor_list.append(successor)
                min_heuristic = successor_heuristic
    return random.choice(successor_list)

def num_of_attacks(board):
    count = 0
    for i in range(1, len(board) - 1):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                count += 1
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1 
    return count

def gen_board():    #index 0 is not used , start at index 1 --> q1, q2..., q8
    board = [0,0,0,0,0,0,0,0,0]
    for i in range(1, len(board)):
        board[i] = random.randint(1, 8) 
    return board

def move(q, pos, board):
    successor = board.copy()
    successor[q] = pos
    return successor

def coolDown(t):
    return 1000 * (0.9**t)       

def compute_prob(E, T):
    return e(E/T)      #Euler's number raised to the power of E/T

def solve(solved, num_of_puzzles):
    percent_solved = (solved / num_of_puzzles) * 100
    return percent_solved

def print_result(cost, solved, num_of_puzzles):
    print('number of puzzles: ' + str(num_of_puzzles) + '\n' 
        + 'solved: ' + str(solved) + '%' + '\n' 
        + 'average search cost: ' + str(cost) + '\n')

def main():
    user_input = int(sys.argv[1])
    hc_solved, hc_cost, sa_solved, sa_cost = board(user_input)
    print('*'*20 + 'Hill Climbing' + '*'*20)
    print_result(hc_cost, hc_solved, user_input)
    print('*'*20 + 'Simulated Annealing' + '*'*20)
    print_result(sa_cost, sa_solved, user_input)

def testing():
    #plateau board --> [0,1,1,4,2,1,8,1,8], good board --> [0,7,4,2,5,8,1,3,6]
    # hc_cost, hc_solved = hill_climbing([0,5,3,2,5,8,1,3,6])
    # hc_solved = solve(hc_solved, 1)
    # print_result(hc_cost, hc_solved, 1)
    sa_cost, sa_solved = sim_annealing([0,6,3,2,5,8,1,3,6])
    sa_solved = solve(sa_solved, 1)
    print_result(sa_cost, sa_solved, 1)

if __name__ == '__main__':
    main()
    #testing()