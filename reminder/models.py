from django.db import models
from django.utils import timezone
import json

class Reminder(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    child_id = models.IntegerField(max_length=100, blank=True, null=True)
    task = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(null=True, default=timezone.now)
    status = models.CharField(max_length=20,default='未提醒')

    class Meta:
        db_table = 'reminder'  # 指定数据库表名，如果你希望使用不同的表名，可以在这里修改

    def __str__(self):
        data = {
            "task": self.task,
            "time": self.time,
            "status": self.status
        }
        return json.dumps(data, ensure_ascii=False)
