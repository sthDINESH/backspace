from django.db import models

# Create your models here.

# workspace model
class WorkSpace(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    # Add more fields as needed, e.g., shape, coordinates for SVG, etc.

    def __str__(self):
        return self.name
