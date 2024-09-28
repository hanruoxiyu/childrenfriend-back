from django.db import models


class Score(models.Model):
    score_id = models.AutoField(primary_key=True)
    child_id = models.IntegerField(null=True, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    enddate = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    child = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'score'
