from video_streamer.models import Video
import find_media_files


MEDIA_ROOT = '/home/beliefs22/PycharmProjects/media'

Video.objects.all().delete()
video_types = [('mp4', 2), ('avi', 1)]
for video_type in video_types:
    current_videos = find_media_files.find_media_files(MEDIA_ROOT, video_type[0])
    if current_videos:
        for found_video in current_videos:
            video_title = found_video.replace(MEDIA_ROOT + "/", "")
            type_of_video = video_type[1]
            relative_path = "{}.{}".format(found_video.replace(MEDIA_ROOT + "/", ""), video_type[0])
            print(video_title, type_of_video, relative_path)
            one_video = Video(video_title, type_of_video, relative_path)
            print("Saving {}".format(video_title))
            one_video.save()

