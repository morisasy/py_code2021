# replace range(len) with enumerate
 players = []
for i in range(len(players)):
    print(i, players[i])

# for i, player in enumerate(players, start =1)
for i, player in enumerate(players):
    print(i, player)


