from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import json


class QA(models.Model):
    QA_id = models.AutoField(primary_key=True)
    child_id = models.IntegerField(verbose_name='孩子id')
    question = models.CharField(max_length=255, verbose_name='问题记录')
    answer = models.CharField(max_length=255, verbose_name='回答记录')
    askTime = models.DateTimeField(default=timezone.now, verbose_name='提问时间')
    child = models.CharField(max_length=10, verbose_name='用户名')

    class Meta:
        db_table = 'QA'
        verbose_name = '问答记录'
        verbose_name_plural = '问答记录'

    def __str__(self):
        data = {
            "question": self.question,
            "answer": self.answer,
            "ask_time": self.ask_time,
            "child": self.child
        }
        return json.dumps(data, ensure_ascii=False)
