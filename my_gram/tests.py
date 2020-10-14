from django.test import TestCase
from .models import Image,Category,Location

# tests
class TestImage(TestCase):
    def setUp(self):
        #location test
        self.location=Location(name='Mali')
        self.location.save_location()
        #category test
        self.category= Category(name ='art')
        self.category.save_category()
        #image test
        self.image = Image(name='creekidy', id=1, description='creekidy rock on creek road', category=self.category, location=self.location)
        self.image.save_image()


    def test_save_image(self):
        self.image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_delete_method(self):
        self.image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, 'image/img.jpg')
        add = Image.objects.filter(image='image/img.jpg')
        self.assertTrue(len(add) > 0)

    def test_search_image_by_category(self):
        self.image.save_image()
        res = self.image.search_by_category(category='art')
        self.assertTrue(len(res) > 0)
        
    def test_filter_image_by_location(self):
        self.image.save_image()
        res = self.image.filter_by_location(location='Mali')
        self.assertTrue(len(res) > 0)

    def test_get_image_by_id(self):
        res = self.image.get_image_by_id(self.image.id)
        image = Image.objects.filter(id=self.image.id)
        self.assertTrue(res, image)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name="art")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
    
    def test_get_category(self):
        self.category.save_category()
        categories = Category.get_category()
        self.assertTrue(len(categories) > 0)

class LocationTestCLass(TestCase):
    def setUp(self):
        self.location = Location(name="mali")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
    
    def test_get_location(self):
        self.location.save_location()
        locations = Location.get_location()
        self.assertTrue(len(locations) > 0)
