
from django.core.management.base import BaseCommand
from octofit_tracker.models.user import User
from octofit_tracker.models.team import Team
from octofit_tracker.models.activity import Activity
from octofit_tracker.models.leaderboard import Leaderboard
from octofit_tracker.models.workout import Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpar dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Criar times
        marvel = Team.objects.create(name='Team Marvel', description='Heróis Marvel')
        dc = Team.objects.create(name='Team DC', description='Heróis DC')

        # Criar usuários
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Criar atividades
        Activity.objects.create(user=tony.email, activity_type='Run', duration=30, date=date.today())
        Activity.objects.create(user=steve.email, activity_type='Swim', duration=45, date=date.today())
        Activity.objects.create(user=bruce.email, activity_type='Bike', duration=60, date=date.today())
        Activity.objects.create(user=clark.email, activity_type='Yoga', duration=20, date=date.today())

        # Criar treinos
        Workout.objects.create(name='Super Strength', description='Heavy lifting', difficulty='Hard')
        Workout.objects.create(name='Shield Training', description='Agility drills', difficulty='Medium')
        Workout.objects.create(name='Bat Endurance', description='Night run', difficulty='Medium')
        Workout.objects.create(name='Kryptonian Cardio', description='Flight sprints', difficulty='Hard')

        # Criar leaderboard
        Leaderboard.objects.create(team=marvel.name, points=700)
        Leaderboard.objects.create(team=dc.name, points=600)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
