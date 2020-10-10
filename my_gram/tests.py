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
    
class CategoryTestClass(TestCase):
    def setUp(self):
        self.categry = Category(name="art")
        self.categry.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.categry, Category))

    def test_save_method(self):
        self.categry.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.categry.save_category()
        self.categry.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.categry.id)
        category.update_category('paint')
        category = Category.get_category_id(self.categry.id)
        self.assertTrue(category.name == 'Paint')

class LocationTestCLass(TestCase):
    def setUp(self):
        self.locashon = Location(name="bahamas")
        self.locashon.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.locashon,Location))

    def test_save_method(self):
        self.locashon.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.locashon.save_location()
        self.locashon.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.locashon.id)
        location.update_location('panama')
        location = Location.get_location_id(self.locashon.id)
        self.assertTrue(location.name == 'panama')