from ._baseCommand import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.user.is_active = False
        self.user.save()
        print(self.style.WARNING(f'{self.user} is deactivate now !'))
