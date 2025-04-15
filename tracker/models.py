from django.db import models

class Position(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.latitude}, {self.longitude} @ {self.timestamp}"