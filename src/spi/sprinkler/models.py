from django.db import models


class Scheduler(models.Model):
    id = models.IntegerField(unique=True, primary_key="True")
    name = models.CharField(max_length=200)
    start_time = models.TimeField()

    def __str__(self):
        return self.name


class Sprinkler(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    order = models.IntegerField()
    scheduler_id = models.ForeignKey(Scheduler, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
