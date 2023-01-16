from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pictures

def index(request):
    pictures = Pictures.objects.all()
    context = {
        'message': 'Welcome my PictureBBS',
        'pictures': pictures,
    }
    return render(request, 'pypicture/index.html', context)

def detail(request, id):
    picture = get_object_or_404(Pictures, pk=id)
    context = {
        'message': 'Show MyPicture ' + str(id),
        'picture': picture,
    }
    return render(request, 'pypicture/detail.html', context)