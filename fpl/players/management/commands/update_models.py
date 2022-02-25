from django.core.management.base import BaseCommand
import pandas as pd
from ...models import Players


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # df = pd.read_csv(
        #    'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/merged_gw.csv')
        df = pd.read_csv(
            'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/gw20.csv')
        model = Players.objects.all()
        for (Name, Club, Type, Point, Minutes, Price) in zip(df.name, df.team, df.position, df.total_points, df.minutes, df.value/10):
            for m in model:
                if(m.name == Name and m.club == Club and m.type == Type):
                    m.price = Price
                    m.save()
            # model=Players(name=Name,club=Club,points=Point,minutes=Minutes,price=Price)
            # model.save()
        #list = []
        #model = Players.objects.all()
        # for d in model:
        #    list.append([d.name, d.club, d.type, d.points])
        # dd = pd.DataFrame(list,
        ##                  columns=('Name', 'Club', 'Type', 'Point')
        #                  )
        #model.to_csv(r'C:\Users\aman\Downloads\data.csv', index=False)
        # print(dd)
        #dd.to_csv(r'C:\Users\aman\Downloads\data.csv', index=False)
