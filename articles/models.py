from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # max_length는 필수 인자
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"제목:{self.title}, 내용:{self.content}"

    