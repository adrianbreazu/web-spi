from django.db import models


class Scheduler(models.Model):
    id = models.IntegerField(unique=True, primary_key="True")
    name = models.CharField(max_length=200)
    start_time = models.TimeField(format("%H:%M"))
    skip_days = models.IntegerField(default=0)
    days = models.CharField(max_length=7, default='MTWTFSS')

    def __str__(self):
        return self.name


class Sprinkler(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    duration = models.IntegerField(default=0)
    order = models.IntegerField()
    GPIO_pin = models.IntegerField(default=0)
    notes = models.CharField(max_length=1000, default="")
    scheduler_id = models.ForeignKey(Scheduler, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order) + "|" + self.name


class Weather(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '|' + str(self.timestamp)

