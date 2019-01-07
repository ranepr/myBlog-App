from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('blogs', views.blogs, name='Blogs'),
    path('contact', views.contact, name='Contact'),
]