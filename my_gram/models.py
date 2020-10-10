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
    def update_image(cls,id,value):
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
        images = Image.objects.filter(category__name__icontains=category)
        return images
    @classmethod
    def filter_by_location(cls, location):
        location = cls.objects.filter(location__id=location)
        return location
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'
        
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Category(models.Model):
    category= models.CharField(max_length=20)
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
    name= models.CharField(max_length=30)
    @classmethod
    def get_location_id(cls, id):
        location = Location.objects.get(pk = id)
        return location
    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
    def update_location(self, update):
        self.name = update
        self.save()
    def delete_location(self):
        self.delete()
