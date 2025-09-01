from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load test data from fixtures'

    def handle(self, *args, **options):
        # Clear old data
        call_command('flush', '--noinput')

        # Load fixtures
        call_command('loaddata', 'categories.json', verbosity=2)
        call_command('loaddata', 'products.json', verbosity=2)

        self.stdout.write(self.style.SUCCESS('✅ Данные успешно загружены!'))

