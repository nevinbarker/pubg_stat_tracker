import matplotlib.pyplot as plt
from matplotlib import rcParams
from io import BytesIO
import base64
from background_task import background
from django.contrib.auth.models import User
import requests
import os
from .models import Stats


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, x_label, y_label, title):
    plt.switch_backend('AGG')
    plt.style.use('fivethirtyeight')
    rcParams.update({'figure.autolayout': True})

    plt.plot(x, y)
    plt.title(title)
    plt.tight_layout()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(x)
    plt.ylim(bottom=0)

    graph = get_graph()
    return graph


@background(schedule=30)
def background_api_call():
    for user in User.objects.all():
        pubgUsername = user.profile.pubgUsername
        userId = user.profile
        if pubgUsername == '':
            pass
        else:
            print("calling API...")
            header = {
                "Authorization": f'Bearer {os.environ.get("PUBG_API_TOKEN")}',
                "Accept": "application/vnd.api+json"
            }
            response = requests.get(f'https://api.pubg.com/shards/steam/players?filter[playerNames]={pubgUsername}',
                                    headers=header)

            context = response.json()

            if 'errors' in context:
                print("PUBG Username invalid.")
            else:
                matches = context['data'][0]['relationships']['matches']['data']

                if len(matches) < 1:
                    pass
                else:
                    for match in matches:
                        matchId = match['id']

                        if Stats.objects.filter(matchId=matchId).filter(user_id=userId).exists():
                            pass
                        else:
                            response = requests.get(f'https://api.pubg.com/shards/steam/matches/{matchId}',
                                                    headers=header)
                            r = response.json()

                            participantList = r["included"]
                            for participant in participantList:
                                if participant["type"] == "participant":
                                    if participant["attributes"]["stats"]["name"] == pubgUsername:
                                        Stats.objects.create(
                                            matchId=matchId,
                                            kills=participant["attributes"]["stats"]["kills"],
                                            deathType=participant["attributes"]["stats"]["deathType"],
                                            damage=participant["attributes"]["stats"]["damageDealt"],
                                            dbno=participant["attributes"]["stats"]["DBNOs"],
                                            revives=participant["attributes"]["stats"]["revives"],
                                            timeAlive=participant["attributes"]["stats"]["timeSurvived"],
                                            user=userId
                                        )
