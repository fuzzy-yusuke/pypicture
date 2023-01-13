from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls), #アドミンページのURLです
    path('', views.index, name='index'),
]