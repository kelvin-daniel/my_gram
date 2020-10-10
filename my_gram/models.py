from django.db import models
from cloudinary.models import CloudinaryField

# app models
class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.ForeignKey('category', on_delete=models.CASCADE,)
    location = models.ForeignKey('location', on_delete=models.CASCADE,)
    image = CloudinaryField('image')
    def save_image(self):
        self.save()
    def update_image(self):
        self.update()
    def delete_image(self):
        self.delete()

    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'
    def __str__(self):
        return self.name

class Category(models.Model):
    category= models.CharField(max_length=20)
    def save_category(self):
        self.save()
    def update_cateory(self):
        self.update()
    def delete_category(self):
        self.delete()
        pass

class Location(models.Model):
    name= models.CharField(max_length=20)
    def save_location(self):
        self.save()
    def update_location(self):
        self.update()
    def delete_location(self):
        self.delete()
        pass
