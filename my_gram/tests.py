from django.test import TestCase
from .models import Image,Category,Location

# tests
class TestImage(TestCase):
    def setUp(self):
        self.location=Location(name='Mali')
        self.location.save_location()
        sel
        self.image = Image(name='creekidy', description='creekidy rock on creek road', category=self.category, location=self.location)
