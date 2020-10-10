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

    def test_save_image(self):
        self.image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_delete_image(self):
        self.image.delete()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('art')
        self.assertTrue(len(images)>0)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='mali')
        self.assertTrue(len(found_images) == 1)
    
    # def test_update_image(self):
    #     self.image.save_image()
    #     image = Image.update_image( self.image.id, 'test update', 'my test',self.loc, self.cat)
    #     upimage = Image.objects.filter(id = self.image.id)
    #     print(upimage)
    #     self.assertTrue(Image.name == 'test update')



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

    def test_update(self):
        new_category = 'paint'
        self.category.update_category(self.category.id, new_category)
        changed_category = Category.objects.filter(name='paint')
        self.assertTrue(len(changed_category) > 0)

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

    def test_update_location(self):
        new_location = 'bahamas'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='bahamas')
        self.assertTrue(len(changed_location) > 0)