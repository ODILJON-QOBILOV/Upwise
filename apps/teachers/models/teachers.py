from django.db import models
from apps.students.models.user import User
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Video(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(upload_to='videos/files')
    image = models.ImageField(upload_to='video/images')
    name = models.CharField(max_length=55)
    description = models.TextField()
    free_or_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class HomeWork(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="homeworks")
    text = models.TextField()

    def __str__(self):
        return self.video.name