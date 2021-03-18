from django.contrib import admin

# Register your models here.
from .models import Tutorial

from .models import TutorialSeries, TutorialCategory

from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_content",
    #           "tutorial_published",
    #           "tutorial_title"
    #           ]

    fieldsets = [("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
    ("URL",{"fields":["tutorial_slug"]}),
    ("Series",{"fields":["tutorial_series"]}),
    ("Content",{"fields":["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)

admin.site.register(Tutorial,TutorialAdmin)

#admin.site.register(Tutorial)