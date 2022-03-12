from django.core.management import BaseCommand
from players.models import Team


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        team = Team.objects.all()
        for t in team:
            t.total_points += t.week_point
            t.week_point = 0
            t.save()
