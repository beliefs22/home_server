from django.conf.urls import url

from . import views

app_name = 'video_streamer'

urlpatterns = [
    # /video_streamer/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<vid>[0-9]+)/$', views.view_single_video, name='view_single_video'),
    url(r'^video_index/$', views.video_index, name='video_index'),
]