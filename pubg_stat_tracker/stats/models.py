from django.db import models


class Stats(models.Model):

    matchId = models.IntegerField()
    kills = models.IntegerFieldField()
    deaths = models.IntegerFieldField()
    damage = models.IntegerFieldField()
    dbno = models.IntegerFieldField()
    revives = models.IntegerFieldField()
    timeAlive = models.IntegerFieldField()
    user = models.ForeignKey('userlogin.Profile', on_delete=models.CASCADE)

