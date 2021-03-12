from django.db import models

# Create your models here.
class Tutorial(models.Model):
    # To limit string lenght, use CharField
    tutorial_title = models.CharField(max_length = 200)
    # No limited length
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    def __str__(self):
        return self.tutorial_title