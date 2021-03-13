from django.contrib import admin

# Register your models here.
from .models import Tutorial

from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_content",
    #           "tutorial_published",
    #           "tutorial_title"
    #           ]

    fieldsets = [("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
    ("Content",{"fields":["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }



admin.site.register(Tutorial,TutorialAdmin)

#admin.site.register(Tutorial)