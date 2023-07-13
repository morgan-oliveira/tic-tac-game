# inicializando tabuleiro
gametable = dict.fromkeys(['a1','a2','a3','a4','a5','a6','a7','a8','a9'], 1)
# como cada movimento seria registrado
def player_one_move_a1(gametable):
    gametable.update({"a1": 1})

# exemplo de win condition
def player_one_win(gametable):
    global playerOneWin
    if (gametable['a1'] and gametable['a2'] and gametable['a3']) == 1:       
        playerOneWin = True 
    else: playerOneWin = False     
player_one_win(gametable)
print(playerOneWin)