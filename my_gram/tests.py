from django.test import TestCase
from .models import Image,Category,Location

# tests
class TestImage(TestCase):
    def setUp(self):
        #location test
        self.location=Location(name='Mali')
        self.location.save_location()
        #category test
        self.category= Category(category='art')
        self.category.save_category()
        #image test
        self.image = Image(name='creekidy', description='creekidy rock on creek road', category=self.category, location=self.location)
        self.image.save_image()

    def test_save_image(self):
        self.image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_delete_image(self):
        self.image.delete()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
    def test_update_image(self):
        pass
    def test_get_image_by_id(self)
    
