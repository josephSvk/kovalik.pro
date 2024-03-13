from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Popis toho, čo príkaz robí'

    def add_arguments(self, parser):
        # Prípadne pridaj argumenty príkazu tu
        pass

    def handle(self, *args, **options):
        # Logika tvojho príkazu
        self.stdout.write(self.style.SUCCESS('Úspešne spustený príkaz!'))