from django.db import models
from django.urls import reverse

class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MakeModel(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'model'
        unique_together = ('make', 'model')

    def __str__(self):
        return f'{self.make} {self.model}'.strip()


class Item(models.Model):
    reference = models.CharField(max_length=255, unique=True)
    make_model = models.ForeignKey(MakeModel, on_delete=models.CASCADE, verbose_name='Make/Model')
    description = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    part_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def name(self):
        return self.description or self.make_model.name

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.reference}: {self.make_model}'
