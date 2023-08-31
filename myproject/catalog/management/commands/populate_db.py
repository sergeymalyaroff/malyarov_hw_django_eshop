from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Populate the database with fixtures'

    def handle(self, *args, **kwargs):
        # вызываем команду `loaddata` для загрузки фикстур.
        # данные загружаю из файла фикстур `categories.json` в каталоге `fixtures`
        call_command('loaddata', 'catalog/fixtures/categories.json')
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
