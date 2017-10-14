from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Video
def index(request):
    return render(request, 'video_streamer/index.html', context={})

def view_single_video(request, video_title):
    video = get_object_or_404(Video, pk=video_title)
    context = {'video' : video }
    return render(request, 'video_streamer/player.html', context=context)

