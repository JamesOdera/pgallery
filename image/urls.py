from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.gallery,name = 'gallery'),
    url(r'^today/$',views.image_of_day,name='imageToday')
]