from django.core.management import BaseCommand
from players.models import Team, Players
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        player = Players.objects.all()
        # df = pd.read_csv(
        #     'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/gw25.csv')
        for p in player:
            p.points = 0
            p.save()
