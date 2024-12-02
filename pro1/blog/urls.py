from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('Read/<int:read_id>/', views.Read, name='Read'), 
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)