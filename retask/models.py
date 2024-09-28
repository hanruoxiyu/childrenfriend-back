from django.db import models

class Retask(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    circle = models.IntegerField(default=1, null=True, blank=True)
    child_id = models.IntegerField(default=1)
    child = models.CharField(max_length=10, null=True, blank=True, default='小明')
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'retask'  # 指定数据库表名
        verbose_name = 'Repeat Task'  # 在Django admin中的显示名称
        verbose_name_plural = 'Repeat Tasks'  # 复数形式的显示名称

    def __str__(self):
        data = {
            "task": self.task,
            "child": self.child,
            "time": self.time,
            "circle": self.circle
        }
        return json.dumps(data, ensure_ascii=False)
