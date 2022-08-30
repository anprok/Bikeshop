from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class League(models.Model):
    name = models.CharField(max_length=32)
    champion = models.ForeignKey(Team, related_name='champion_of', on_delete=models.CASCADE)
    number_of_teams = models.PositiveIntegerField()

    class Meta:
        app_label = 'tournament'