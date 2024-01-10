from django.db import models

class RSVP(models.Model):
    attending = models.BooleanField()
    name = models.TextField(max_length=500)
    dietary_restrictions = models.TextField(blank=True)
    observations = models.TextField(blank=True)

    def __str__(self):
        return f"RSVP by {self.name}"
