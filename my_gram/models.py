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
    def update_image(self):
        pass

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,category):
        searched_images = cls.objects.filter(category__name__icontains=category)
        return searched_images

    def get_image_by_id(cls):
        images = cls.objects.all()
        return images
   
    def filter_by_location(cls,location):
        location = Image.objects.filter(location__name=location).all()
        return location

    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_category(cls):
        category = Category.objects.all()
        return category

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=40)

    @classmethod
    def get_location_id(cls):
        location = Location.objects.all()
        return location

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
