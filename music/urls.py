from django.urls import path, re_path
from . import views

app_name= 'music'

urlpatterns = [
        # /music/
        path('', views.IndexView.as_view(), name='index'),
        #User registration form
        re_path(r'^register/$',views.UserFormView.as_view(),name='register'),
        # /music/id_no/
        re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # /music/album/add/
        re_path(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),
        # For updating a given album /music/album/id of updated album
        re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name='album-update'),
        #For deleting a album
        re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name='album-delete'),
]