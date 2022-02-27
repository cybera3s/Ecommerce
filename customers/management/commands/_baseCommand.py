from django.core.management import BaseCommand, CommandError

from core.models import User


class Command(BaseCommand):
    help = 'activate a user'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?')

    def handle(self, *args, **options):

        try:
            self.user = User.objects.get(username=options['username'])
        except User.DoesNotExist:
            raise CommandError('Invalid Username!')


