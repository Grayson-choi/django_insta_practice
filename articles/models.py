from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # max_length는 필수 인자
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"제목:{self.title}, 내용:{self.content}"

    