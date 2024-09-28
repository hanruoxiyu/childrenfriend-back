from django.db import models

class ZuoZi(models.Model):
    zuozi_id = models.AutoField(primary_key=True)
    child_id = models.IntegerField(null=True, blank=True)
    tupianpath = models.CharField(max_length=255, null=True, blank=True)
    costime = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    remind = models.IntegerField(null=True, blank=True)
    child = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'zuozi'
