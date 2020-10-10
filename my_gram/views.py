from django.shortcuts import render,redirect
from models import Image,Category,Location
from django.http import HttpResponse,Http404

# views
def index(request):
    location= Location.objects.all()
    images= Image.objects.all()
    title='Picsabay'
    return render(request, 'my_gram/index.html',{'title':title,'images':images, 'location':location}})


def location_filter(request, image_location):
    locs = Location.get_location_id(image_location)
    location = Location.objects.all()
    images = Image.filter_by_location(image_location)
    title = f'Picsabay {location}'
    return render(request, 'my_gram/location.html', {'title':title, 'images':images, 'location':location, 'locs':locs})

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
    return render(request,"my_gram/single.html",{'title':title,"image":image, "location":location, "category":category})

def search_image(request):
    title = 'Search Picsabay'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'my_gram/search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = "Didn't find anything to search"
        return render(request, 'my_gram/search.html',{"message": message})