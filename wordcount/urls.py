

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homep'),
    path('about/',views.about , name='abu'),
    path('count/',views.count, name='count')
]
