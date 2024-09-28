from django.db import models
from django.utils import timezone
import json

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="科目")
    question_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="考题")
    answer = models.CharField(max_length=255, blank=True, null=True, verbose_name="答案")

    def __str__(self):
        data = {
            "question_id": self.question_id,
            "subject": self.subject,
            "question_text": self.question_text,
            "answer": self.answer
        }
        return json.dumps(data, ensure_ascii=False)

    class Meta:
        db_table = 'question'
        managed = True  # 如果你希望Django管理这个表（包括迁移等），则应设置为True。对于已存在的表，默认设置为False。
