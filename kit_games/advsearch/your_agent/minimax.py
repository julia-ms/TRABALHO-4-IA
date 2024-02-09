from argparse import Action
import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    
    def max_value(state, alpha, beta, depth):
        if state.is_terminal() or depth == 0:
            return eval_func(state, state.player), state
        v = float('-inf')
        for move in state.legal_moves():
            value, action = min_value(state.next_state(move), alpha, beta, depth-1)
            v = max(v,value)
            if v >= beta:
                return v,state
        return v,state
    
    def min_value(state, alpha, beta, depth):
        if state.is_terminal() or depth == 0:
            return eval_func(state, None),state
        v = float('inf')
        for move in state.legal_moves():
            value , action = max_value(state.next_state(move), alpha, beta, depth-1)
            v = min(v, value)
            if v <= alpha:
                return v,state
        return v,state
    
    
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    raise NotImplementedError()
