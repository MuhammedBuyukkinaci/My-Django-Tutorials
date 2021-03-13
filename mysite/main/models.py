from django.db import models
from django.utils import timezone

# Create your models here.
class Tutorial(models.Model):
    # To limit string lenght, use CharField
    tutorial_title = models.CharField(max_length = 200)
    # No limited length
    tutorial_content = models.TextField()
    #tutorial_published = models.DateTimeField("date published")
    tutorial_published = models.DateTimeField("date published",default = timezone.now )

    def __str__(self):
        return self.tutorial_title