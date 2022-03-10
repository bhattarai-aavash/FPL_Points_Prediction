from django.core.management import BaseCommand
from players.models import Team, Players
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        team = Team.objects.all()
        player = Players.objects.all()
        df = pd.read_csv(
            'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/gw25.csv')

        # weekly update from csv
        for p in player:
            for (Name, Club, Type, Point, Minutes, Price) in zip(df.name, df.team, df.position, df.total_points, df.minutes, df.value/10):
                if (p.name == Name and p.club == Club and p.type == Type):
                    p.points += Point
                    p.minutes = Minutes
                    p.save()
        #             # print(Point)

        # Points to zero
        # for p in player:
        #     p.points = 0
        #     p.save()
