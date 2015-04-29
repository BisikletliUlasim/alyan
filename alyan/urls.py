from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^edit_bicycle/(?P<bicycle_id>[0-9])/', views.edit_bicycle, name='edit_bicycle'),
    url(r'^my_bicycles/', views.my_bicycles, name='my_bicycles'),
]