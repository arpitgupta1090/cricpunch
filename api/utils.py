from api.cricpunch import Series, Match
from api.models import TransactionCount
import re
import datetime


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


def get_urls():
    data = {

        'api/series/': 'List of all series',
        'api/series/<series_id>': 'Describe particular series with list of all matches',
        'api/match/<match_id>': 'Describe particular Match with scorecard and other details',
        'api/players/<series_id>': 'List of all players in a particular series',
    }
    return data


def update_transaction(username):

    try:
        queryset = TransactionCount.objects.get(user=username)
        result = limit_check(queryset)
        if result[0] and result[1] == "day":
            queryset.dailyCount += 1
            queryset.monthlyCount += 1
            queryset.yearlyCount += 1
            queryset.save()
            return True,
        elif result[0] and result[1] == "month":
            queryset.dailyCount = 1
            queryset.monthlyCount += 1
            queryset.yearlyCount += 1
            queryset.save()
            return True,
        elif result[0] and result[1] == "year":
            queryset.dailyCount = 1
            queryset.monthlyCount = 1
            queryset.yearlyCount += 1
            queryset.save()
            return True,
        elif result[0]:
            queryset.dailyCount = 1
            queryset.monthlyCount = 1
            queryset.yearlyCount = 1
            queryset.save()
            return True,
        else:
            return False, result[1]
    except TransactionCount.DoesNotExist:
        queryset = TransactionCount(user=username)
        queryset.save()
        return True,
    except Exception as e:
        return False, str(e)


def limit_check(queryset):

    daily_limit = 100
    monthly_limit = 2500
    yearly_limit = 25000
    today = datetime.date.today()
    today_day = today.strftime("%d")
    today_month = today.strftime("%m")
    today_year = today.strftime("%Y")
    user_day = queryset.modifiedDate.strftime("%d")
    user_month = queryset.modifiedDate.strftime("%m")
    user_year = queryset.modifiedDate.strftime("%Y")
    result = True, "day"

    if today_year == user_year:
        if queryset.yearlyCount >= yearly_limit:
            result = False, "Yearly limit exceeded"
        if today_month == user_month:
            if queryset.monthlyCount >= monthly_limit:
                result = False, "Monthly limit exceeded"
            if today_day == user_day:
                if queryset.dailyCount >= daily_limit:
                    result = False, "Daily limit exceeded"
            else:
                result = True, "month"
        else:
            result = True, "year"
    else:
        result = True, False

    return result
