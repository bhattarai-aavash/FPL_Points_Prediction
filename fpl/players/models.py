from re import T
from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    points = models.IntegerField()
    minutes = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Players, related_name='team', blank=True)
    subs = models.ManyToManyField(Players, related_name='extras')
    total_points = models.IntegerField()
    week_point = models.IntegerField(default=0)
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, null=True, blank=True)
    transfer_counter = models.IntegerField(default=1)
    captain = models.OneToOneField(
        Players, on_delete=models.CASCADE, null=True, related_name='captain')

    def __str__(self):
        return f'{self.name}'
