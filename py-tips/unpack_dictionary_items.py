# use items() to directly unpack dictionary values

teams_by_color = {"blue": ["Zaki", "Samir"]}
player_list = []
def is_winning(team_color, false=None):
    if team_color:
        return True
    return False

def advance_level(players):

    if players is None:
        return player_list + players
    return None


for team_color, players in teams_by_color.items():
    if is_winning(team_color):
        advance_level(players)