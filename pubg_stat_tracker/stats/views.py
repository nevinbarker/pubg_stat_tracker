from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.views.generic.list import ListView
from .models import Stats
from django.contrib import messages


@login_required
def stats(request):
    header = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNGFiYTExMC00YjIyLTAxMzktZmU3YS0wZDExNzBkZGYxZjMiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjEyNjY4NzE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1Ymdfc3RhdF90cmFjIn0.sKeF4EzTsxy714VEaWY5n19j35vsJvH15gTzBb7cmH0",
        "Accept": "application/vnd.api+json"
    }
    pubgUsername = request.user.profile.pubgUsername

    if pubgUsername == '':
        messages.warning(request, "You haven't linked your PUBG account. Go to the profile page to link your account.")
    else:
        response = requests.get(f'https://api.pubg.com/shards/steam/players?filter[playerNames]={pubgUsername}',
                                headers=header)

        context = response.json()

        if 'errors' in context:
            messages.warning(request, "There is no PUBG account with that username. make sure your PUBG username is correct in your profile page.")
        else:
            matches = context['data'][0]['relationships']['matches']['data']

            if len(matches) < 1:
                pass
            else:
                for match in matches:
                    matchId = match['id']

                    if Stats.objects.filter(matchId=matchId).exists():
                        pass
                    else:
                        response = requests.get(f'https://api.pubg.com/shards/steam/matches/{matchId}')
                        r = response.json()
                        Stats.objects.create(
                            matchId=matchId,
                        )

    return render(request, 'stats/stats.html', {
        'playerName': pubgUsername
    })


class StatsListView(ListView):
    model = Stats
    template_name = 'stats/stats.html'

# pubg api key:
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNGFiYTExMC00YjIyLTAxMzktZmU3YS0wZDExNzBkZGYxZjMiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjEyNjY4NzE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1Ymdfc3RhdF90cmFjIn0.sKeF4EzTsxy714VEaWY5n19j35vsJvH15gTzBb7cmH0