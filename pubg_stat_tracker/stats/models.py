from django.db import models


class Stats(models.Model):

    matchId = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    damage = models.IntegerField()
    dbno = models.IntegerField()
    revives = models.IntegerField()
    timeAlive = models.IntegerField()
    user = models.ForeignKey('userlogin.Profile', on_delete=models.CASCADE)

