from django.core.management.base import BaseCommand
import pandas as pd
from ...models import Players


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv(
            'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/merged_gw.csv')
        for (Name, Club, Type, Point) in zip(df.name, df.team, df.position, df.total_points):
            model = Players(name=Name, club=Club, type=Type, points=Point)
            model.save()
