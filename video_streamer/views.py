from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Video
def index(request):
    return render(request, 'video_streamer/index.html', context={})

def view_single_video(request, vid):
    video = get_object_or_404(Video, pk=vid)
    context = {'video' : video }
    return render(request, 'video_streamer/player.html', context=context)


def video_index(request):
    all_videos = Video.objects.all()
    context = {'all_videos' : all_videos}
    return render(request, 'video_streamer/video_index.html', context=context)