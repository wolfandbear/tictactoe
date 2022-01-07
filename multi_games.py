import tictactoe

no_games = 0
winner = None
no_x = 0
no_o = 0
tie = 0

while no_games < 3:

    winner = tictactoe.main()

    if winner == 'X':
        no_x += 1
    elif winner == 'O':
        no_o += 1
    elif winner == 'tie':
        tie += 1
    print('**X: ', no_x, '  **O: ', no_o, '  **tie ', tie)

    no_games += 1
