from argparse import Action
import random
from typing import Tuple, Callable


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:

    def max_value(state, alpha, beta, depth):
        if state.is_terminal() or depth == 0:           
            return eval_func(state, state.player), None
        v = float('-inf')
        for move in state.legal_moves():
            value, _ = min_value(state.next_state(move), alpha, beta, depth - 1)
            v = max(v, value)
            if v >= beta:
                return v, None
            alpha = max(alpha, v)
        return v, None

    def min_value(state, alpha, beta, depth):
        if state.is_terminal() or depth == 0:
            return eval_func(state, None), None
        v = float('inf')
        for move in state.legal_moves():
            value, _ = max_value(state.next_state(move), alpha, beta, depth - 1)
            v = min(v, value)
            if v <= alpha:
                return v, None
            beta = min(beta, v)
        return v, None

    best_move = None
    best_value = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in state.legal_moves():
        value, _ = min_value(state.next_state(move), alpha, beta, max_depth - 1)

        if value > best_value:
            best_value = value
            best_move = move

        alpha = max(alpha, best_value)

    return best_move
