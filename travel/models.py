from django.db import models
from django.utils import timezone
import json
# Create your models here.

class Travel(models.Model):
    plan_id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=True, default=timezone.now)
    child_id = models.IntegerField(default=1)
    destination = models.CharField(max_length=255, null=True, blank=True)
    startlocation = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'travel'  # 指定数据库表名

    def __str__(self):
        data = {
            "time": self.time,
            "destination": self.destination,
            "startlocation": self.startlocation
        }
        return json.dumps(data, ensure_ascii=False)

