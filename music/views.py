from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from .models import Album
#from django.template import loader
from django.shortcuts import render
from django.http import Http404

def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request, 'music/index.html',{'all_albums': all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("404 Object Not found! ")
    return render(request, 'music/details.html', {'album': album})