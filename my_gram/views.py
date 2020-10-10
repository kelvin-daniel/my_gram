from django.shortcuts import render
from models import Image

# views
def home(request):
    images= Image.objects.all()
    return render(request, 'my_gram/home.html', {'images':images})