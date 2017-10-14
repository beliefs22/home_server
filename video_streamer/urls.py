from django.conf.urls import url

from . import views

app_name = 'video_streamer'

urlpatterns = [
    # /video_streamer/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<video_title>[0-9a-zA-Z_]+)/$', views.view_single_video, name='view_single_video'),
]