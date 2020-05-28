from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="westriver").exists():
            User.objects.create_superuser(username="westriver", email="westriver.naoki0316@gmail.com", password="3naC1oR6ki")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
        if not User.objects.filter(username="Hidakankuro").exists():
            User.objects.create_superuser(username="Hidakankuro", email="1764689339@g.ecc.u-tokyo.ac.jp", password="jojolion9wasawasa ")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
        if not User.objects.filter(username="admin_taniguchi").exists():
            User.objects.create_superuser(username="admin_taniguchi", email="taniguchi-shunya0218@g.ecc.u-tokyo.ac.jp", password="Idjen390id?")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))