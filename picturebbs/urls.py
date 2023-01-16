from django.urls import path
from . import views

app_name='pypicture'

urlpatterns = [
    #path('admin/', admin.site.urls), #アドミンページのURLです
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
]