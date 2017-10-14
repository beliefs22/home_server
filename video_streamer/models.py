from django.db import models

# Create your models here.


class Video(models.Model):
    vid = models.CharField(max_length=200, primary_key=True)
    video_title = models.CharField(max_length=200)
    OGG = 0
    WEBM = 1
    MP4 = 2
    FLASH = 3
    VIDEO_TYPE = (
        (OGG, 'video/ogg'),
        (WEBM, 'video/webm'),
        (MP4, 'video/mp4'),
        (FLASH, 'video/flv'),
    )

    video_type = models.IntegerField(
        choices=VIDEO_TYPE,
        default=WEBM,
        help_text="The Video type"
    )
    video_file = models.FileField(
        upload_to="",
        help_text="The file you wish to upload. Make sure that it's the correct format."
    )

    def get_type(self):
        video_types = {
            0 :'video/ogg',
            1 :'video/webm',
            2 :'video/mp4',
            3 :'video/flv',
        }
        return video_types[self.video_type]

    def __repr__(self):
        return self.video_title

    def __str__(self):
        return self.video_title

