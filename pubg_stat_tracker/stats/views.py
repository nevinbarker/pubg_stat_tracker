from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def stats(request):
    header = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNGFiYTExMC00YjIyLTAxMzktZmU3YS0wZDExNzBkZGYxZjMiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjEyNjY4NzE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1Ymdfc3RhdF90cmFjIn0.sKeF4EzTsxy714VEaWY5n19j35vsJvH15gTzBb7cmH0",
        "Accept": "application/vnd.api+json"
    }
    playerName = 'mrwafflesman'
    response = requests.get(f'https://api.pubg.com/shards/steam/players?filter[playerNames]={playerName}', headers=header)

    context = response.json()

    matches = context['data'][0]['relationships']['matches']['data']

    if len(matches) < 1:
        print('no matches')
    else:
        for match in matches:
            matchId = match['id']
            response = requests.get(f'https://api.pubg.com/shards/steam/matches/{matchId}')
            r = response.json()

    return render(request, 'stats/stats.html', {
        'playerName': context['data'][0]['attributes']['name']
    })


# pubg api key:
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNGFiYTExMC00YjIyLTAxMzktZmU3YS0wZDExNzBkZGYxZjMiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjEyNjY4NzE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1Ymdfc3RhdF90cmFjIn0.sKeF4EzTsxy714VEaWY5n19j35vsJvH15gTzBb7cmH0