Caue Scotti Luciano Rocha (00338597)
Galeano Folle Domingues (00334948)
Júlia Mombach da Silva (00281023) 

Nenhuma biblioteca adicional precisa ser instalada.

Resultados:
Tic-Tac-Toe
(i) O minimax sempre ganha do randomplayer? 
    R.: Testamos 3 vezes com o randomplayer sendo o primeiro jogador e 3 vezes com o minimax sendo o primeiro. Em todas o minimax ganhou.

(ii) O minimax sempre empata consigo mesmo?
    R.: Testamos 3 vezes e sempre deu empate. 

(iii) Site não abriu


Othello

(i) Represente em uma matriz de 3 X 3 onde as linhas representam o jogador que inicia
(player 1) e as colunas representam o player 2 e em cada célula, indique se a partida
resultou em vitória (1), derrota (-1) ou empate (0) entre os agentes com cada uma das
heurísticas.

|        | Count | Mask | Custom |
| Count  |   1   |  1   |   1    |
| Mask   |   1   |  1   |   1    |
| Custom |   1   |  0   |   1    |

(ii) Observe e relate qual implementação foi a mais bem-sucedida.
    R.: Dos 9 testes, o jogador que começou jogando ganhou em 8. Apenas no custom x mask a heuristica mask conseguiu empatar mesmo sendo o segundo jogador. 

(iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de
performance.
    R.: O mask parece ser um algoritmo um pouco mais eficiente, porque não só leva em consideração o número de peças no tabuleiro, mas também da pontos para suas posições. 


Feedback: 
O trabalho foi de fácil implementação, passamos um pouco de dificuldade apenas para fazer debug da função minimax. Utilizamos chatGPT apenas para entender melhor o funcionamento da função minimax.
