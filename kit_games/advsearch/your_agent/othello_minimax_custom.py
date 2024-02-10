import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move
from .othello_minimax_count import evaluate_count
from .othello_minimax_mask import evaluate_mask

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.



def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.
    
    return minimax_move (state, 5, evaluate_custom)

def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """

    # player_mobility = len(state.board.legal_moves(player))
    # opponent_mobility = len(state.board.legal_moves(state.board.opponent(player)))

    # return player_mobility - opponent_mobility
    
    jogadas = 0
    state_copy = state.board.copy()
    for jogada_player in state.legal_moves():
        state_copy.process_move(jogada_player, "W" if player == "W" else "B")
        for jogada_adversario in state_copy.legal_moves("W" if player == "W" else "B"):
            jogadas += 1
            state_copy = state.board.copy()
    
    return 64 - jogadas

   

