from django.db import models
import json

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    score_id = models.IntegerField(blank=True, null=True)
    useranswer = models.CharField(max_length=255, null=True, blank=True)
    iscorrect = models.CharField(max_length=2, choices=[('正确', '正确'), ('错误', '错误')], null=True)
    question_text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'exam'

    def __str__(self):
        data = {
            "useranswer": self.useranswer,
            "iscorrect": self.iscorrect,
            "question_text": self.question_text,
            "answer": self.answer,
        }
        return json.dumps(data, ensure_ascii=False)
