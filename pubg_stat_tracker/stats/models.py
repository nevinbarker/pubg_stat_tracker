from django.db import models


class Stats(models.Model):

    matchId = models.CharField(max_length=50, blank=True)
    kills = models.IntegerField()
    deathType = models.CharField(max_length=12, blank=True)
    damage = models.IntegerField()
    dbno = models.IntegerField()
    revives = models.IntegerField()
    timeAlive = models.IntegerField()
    user = models.ForeignKey('userlogin.Profile', on_delete=models.CASCADE)

