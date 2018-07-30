from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)


class MakeModel(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('make', 'model')


