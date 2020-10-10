from django.db import models
from cloudinary.models import CloudinaryField

# app models
class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.ForeignKey('category', on_delete=models.CASCADE,)
    location = models.ForeignKey('location', on_delete=models.CASCADE,)
    image = CloudinaryField('image')

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(category__name__icontains = category)
        return images
        
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location)
        return image_location
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=20)
    @classmethod
    def get_category_id(cls, id):
        category=Category.objects.get(pk = id)
        return category
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def update_category(self, update):
        self.name = update
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=30)
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    def delete_location(self):
        self.delete()
