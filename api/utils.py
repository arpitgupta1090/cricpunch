from api.cricpunch import Series, Match
import re


def all_series():
    data = list()
    series = Series()
    pattern1 = '^/series/_/id/+'
    pattern2 = '^/series/.+/.+'
    pattern3 = '^/series/.+'
    pattern4 = '.*/series/.*'

    for i in series.all_series:
        if re.match(pattern1, i):
            series_name = re.split('/id/', i)[1].split('/')[-1]
            series_id = re.split('/id/', i)[1].split('/')[0]
            dct = {'ref': i, 'name': series_name, 'id': series_id}
            data.append(dct)

        elif re.match(pattern2, i):
            series_name = i.split('/')[2]
            series_id = i.split('/')[2].split('-')[-1]
            dct = {'ref': i, 'name': series_name, 'id': series_id}
            data.append(dct)

        elif re.match(pattern3, i):
            series_name = i.split('/')[2]
            series_id = i.split('/')[2].split('-')[-1]
            dct = {'ref': i, 'name': series_name, 'id': series_id}
            data.append(dct)

        elif re.match(pattern4, i):
            series_name = i.split('/')[-1]
            series_id = i.split('/')[3]
            dct = {'ref': i, 'name': series_name, 'id': series_id}
            data.append(dct)
        else:
            dct = {'ref': i, 'name': None, 'id': None}
            data.append(dct)
    return data


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
