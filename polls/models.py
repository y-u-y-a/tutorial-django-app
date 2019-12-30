from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # strオブジェクトに変換する特殊メソッド
    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
