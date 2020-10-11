from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import HttpResponse,Http404

# views
def index(request):
    images= Image.objects.all()
    locations = Location.get_locations()
    category = Category.get_category()
    title='Picsabay'
    return render(request, 'index.html',{'title':title,'images':images, 'locations': locations, 'category': category})


def location_filter(request, location):
    images = Image.filter_by_location(location)
    print(images)
    title = f'Picsabay {location}'
    return render(request, 'location.html', {'title':title, 'images':images})

def single(request,category_name,image_id):
    # images
    title='Picsabay'
    location=Location.objects.all()
    # categories
    category = Image.objects.filter(category__name = category_name)
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single.html",{'title':title,"image":image, "location":location, "category":category})

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'Did not find anything to search'
        return render(request, 'search.html',{"message": message})