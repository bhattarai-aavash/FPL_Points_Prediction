from django.core.management import BaseCommand
from players.models import Team


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        team = Team.objects.all()
        for t in team:
            if t.transfer_counter <= 0:
                t.total_points += t.transfer_counter*4
                print(t.transfer_counter*4)
                t.transfer_counter = 1
                t.save()
