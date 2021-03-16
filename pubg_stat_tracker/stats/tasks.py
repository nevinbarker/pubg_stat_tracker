import time
from django.utils import timezone
from background_task import background
from django.contrib.auth.models import User
import requests
import os
from .models import Stats


# @background(schedule=timezone.now())
# def background_api_call():
#    for user in User.objects.all():
#        pubgUsername = user.profile.pubgUsername
#        userId = user.profile
#        if pubgUsername == '':
#            pass
#        else:
#            print("calling API for player...")
#            header = {
#                "Authorization": f'Bearer {os.environ.get("PUBG_API_TOKEN")}',
#                "Accept": "application/vnd.api+json"
#            }
#            response = requests.get(f'https://api.pubg.com/shards/steam/players?filter[playerNames]={pubgUsername}',
#                                    headers=header)
#
#            context = response.json()
#
#            if 'errors' in context:
#                print("PUBG Username invalid.")
#            else:
#                matches = context['data'][0]['relationships']['matches']['data']
#
#                if len(matches) < 1:
#                    pass
#                else:
#                    for match in matches:
#                        matchId = match['id']
#
#                        if Stats.objects.filter(matchId=matchId).filter(user_id=userId).exists():
#                            pass
#                        else:
#                            print("calling API for matches...")
#                            response = requests.get(f'https://api.pubg.com/shards/steam/matches/{matchId}',
#                                                    headers=header)
#                            r = response.json()
#
#                            participantList = r["included"]
#                            for participant in participantList:
#                                if participant["type"] == "participant":
#                                    if participant["attributes"]["stats"]["name"] == pubgUsername:
#                                        Stats.objects.create(
#                                            matchId=matchId,
#                                            kills=participant["attributes"]["stats"]["kills"],
#                                            deathType=participant["attributes"]["stats"]["deathType"],
#                                            damage=participant["attributes"]["stats"]["damageDealt"],
#                                            dbno=participant["attributes"]["stats"]["DBNOs"],
#                                            revives=participant["attributes"]["stats"]["revives"],
#                                            timeAlive=participant["attributes"]["stats"]["timeSurvived"],
#                                            user=userId
#                                        )
#                            time.sleep(r.elapsed.total_seconds())
