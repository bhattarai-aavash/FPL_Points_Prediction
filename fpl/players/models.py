from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    points = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Players, related_name='team')
    total_points = models.IntegerField()
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
