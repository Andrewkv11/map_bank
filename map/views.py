from django.shortcuts import render
from .folium_map import create_map


# Create your views here.
def index(request):
    context = {
        'map': create_map(),
    }
    return render(request, 'map/index.html', context=context)
