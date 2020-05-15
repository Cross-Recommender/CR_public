from django.db import models

# Create your models here.
from django.db import models


class Diary(models.Model):
    text = models.TextField('日記')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.CharField('コメント', max_length=300)
    target = models.ForeignKey(Diary, on_delete=models.CASCADE, verbose_name='紐づく日記')
    created_at = models.DateTimeField(auto_now_add=True)