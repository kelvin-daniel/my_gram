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

    def search_image(category):
        pass

    @classmethod
    def search_by_category(cls,search_term):
        searched_images = cls.objects.filter(category__icontains = search_term)
        return searched_images

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
    
    def filter_by_location(location):
        pass

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
        category = Category.objects.get(pk = id)
        return category

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
    name = models.CharField(max_length=50)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

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
