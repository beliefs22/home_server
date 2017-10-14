from video_streamer.models import Video
import find_media_files


MEDIA_ROOT = '/home/beliefs22/PycharmProjects/media'

Video.objects.all().delete()
video_types = [('mp4', 2), ('avi', 1)]
vid = 1
for video_type in video_types:
    current_videos = find_media_files.find_media_files(MEDIA_ROOT, video_type[0])
    current_videos = sorted(list(current_videos))
    if current_videos:
        for found_video in current_videos:
            video_title = found_video.replace(MEDIA_ROOT + "/", "")
            type_of_video = video_type[1]
            relative_path = "{}.{}".format(found_video.replace(MEDIA_ROOT + "/", ""), video_type[0])
            print(vid, video_title, type_of_video, relative_path)
            one_video = Video(vid, video_title, type_of_video, relative_path)
            print("Saving {}".format(found_video))
            one_video.save()
            vid += 1

