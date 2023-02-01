from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pictures
from .forms import SearchForm
from .forms import PictureForm

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        pictures = Pictures.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        pictures = Pictures.objects.all()
    context = {
        'message': 'Welcome my PictureBBS',
        'pictures': pictures,
        'searchForm':searchForm,
    }
    return render(request, 'pypicture/index.html', context)

def detail(request, id):
    picture = get_object_or_404(Pictures, pk=id)
    context = {
        'message': 'Show MyPicture ' + str(id),
        'picture': picture,
    }
    return render(request, 'pypicture/detail.html', context)

def new(request):
    pictureForm = PictureForm()
    context = {
        'message': 'New MyPicture',
        'pictureForm': pictureForm,
    }
    return render(request, 'pypicture/new.html', context)

def create(request):
    if request.method == 'POST':
        pictureForm = PictureForm(request.POST)
        if pictureForm.is_valid():
            picture = pictureForm.save()
    context = {
        'message': 'Upload Picture' + str(picture.id),
        'picture': picture,
    }
    return render(request, 'pypicture/detail.html', context)

def edit(request, id):
    picture = get_object_or_404(Pictures, pk=id)
    pictureForm = PictureForm(instance=picture)

    context = {
        'message': '投稿を編集する',
        'picture': picture,
        'pictureForm': pictureForm,
    }
    return render(request, 'pypicture/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        picture = get_object_or_404(Pictures, pk=id)
        pictureForm = PictureForm(request.POST, instance=picture)
        if pictureForm.is_valid():
            pictureForm.save()
    context = {
        'message': str(id) + 'を更新しました',
        'picture': picture,
    }
    return render(request, 'pypicture/detail.html', context)

def delete(request, id):
    picture = get_object_or_404(Pictures, pk=id)
    picture.delete()

    pictures = Pictures.objects.all()
    context = {
        'message': 'Delete MyPicture ' + str(id),
        'pictures': pictures,
    }
    return render(request, 'pypicture/index.html', context)
