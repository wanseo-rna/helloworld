def rps_low(player1, player2):
    outcomes = {
        ('rock', 'scissors'): 'player1',
        ('scissors', 'paper'): 'player1',
        ('paper', 'rock'): 'player1',
        ('scissors', 'rock'): 'player2',
        ('paper', 'scissors'): 'player2',
        ('rock', 'paper'): 'player2',
    }
    if player1 == player2:
        return 'draw'
    return outcomes.get((player1, player2), 'invalid')

def rps_high(player1, player2):
    if player1 == 'rock':
        if player2 == 'rock':
            return 'draw'
        elif player2 == 'scissors':
            return 'player1'
        elif player2 == 'paper':
            return 'player2'
        else:
            return 'invalid'
    elif player1 == 'scissors':
        if player2 == 'rock':
            return 'player2'
        elif player2 == 'scissors':
            return 'draw'
        elif player2 == 'paper':
            return 'player1'
        else:
            return 'invalid'
    elif player1 == 'paper':
        if player2 == 'rock':
            return 'player1'
        elif player2 == 'scissors':
            return 'player2'
        elif player2 == 'paper':
            return 'draw'
        else:
            return 'invalid'
    else:
        return 'invalid'