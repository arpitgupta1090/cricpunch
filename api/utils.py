from api.cricpunch import Series, Match


def all_series():
    series = Series()
    return series.all_series


def get_series(sid):
    series = Series(sid)
    data = {'name': series.name, 'matches': series.matches, 'players': series.players}
    return data


def get_match(mid):
    match = Match(mid)
    data = {
        'description': match.description,
        'status': match.status,
        'series_id': match.series_id,
        'match_id': match.match_id,
        'series_name': match.series_name,
        'title': match.title,
        'squads': match.squads,
        'score': match.score
    }
    return data


def get_players(sid):
    series = Series(sid)
    data = list()

    for team in series.players:
        for player in team:
            team = player.get("player_team")
            player_id = player.get("player_id")
            player_name = player.get("player_name")
            dct = {'team': team, 'player_id': player_id, 'player_name': player_name}
            data.append(dct)

    return data
