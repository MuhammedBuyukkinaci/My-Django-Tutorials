# My-Django-Tutorials

## Intro

1) Use the command below to list main functions of django:

```shellscript
django-admin
```

2) In django, a website is composed of apps. The website is collections of apps.

3) To start a new project. After this commands run, a new app named mysite is also going to be created and app named main is the primary app.

```shellscript
django-admin startproject mysite
```

4) To create an app in the project. After that,

```shellscript
python manage.py startapp main
```

5) To run our development server

```shellscript
python manage.py runserver
```

6) Controller takes the URL and maps it onto a view. View returns the template.
 

7) Firstly, a URL goes to mywebsite/urls.py. Secondly, it checks a corresponding pattern in *urlpatterns* list. Thirdly, it goes to corresponding url pattern's directory (main/urls.py in this case). Fourthly, it goes from main/urls.py to main/view.py and looks for corresponding function which was called in main/urls.py. Then it returns the return of that function in main/views.py

## Models

8) The importance of models in Django comes from models. Model is the way to interact with DB.

9) To change DB configurations, go to mysite/settings.py. sqlite3 is the default DB for Django. We can switch to MySQL or PostgreSQL.

11) After adding a new app, first install the app and then add model. To install the app named *main*, add 'main.apps.MainConfig' to **INSTALLED_APPS** list in **mysite/settings.py** file.

11) Every time we create a new model, we also have a new table in DB. After creating a new model or editing an existent model, we should make migration via

```shellscript
python manage.py makemigrations
```

12) To make SQL ready after migrations(not used frequently)

```shellscript
python manage.py sqlmigrate 0001
```

13) After applying makemigrations to models, run the following to activate SQL changes(used frequently)

```shellscript
python manage.py migrate
```

14) 3 steps to deal with models
    - Do sometihng with models
    - makemigrations
    - migrate

15) To interactively interact with our website

```shellscript
python manage.py shell
```

```python
from main.models import Tutorial
Tutorial.objects.all()
#<QuerySet []>
from django.utils import timezone
new_tutorial = Tutorial(tutorial_title = "To be", tutorial_content = "...or not to be", tutorial_published =timezone.now())
new_tutorial.save() # it is like commit in SQL
Tutorial.objects.all()
#<QuerySet [<Tutorial: To be>]>

```

## Admin and Apps

16) To create a superuser

```shellscript
python manage.py createsuperuser
```

17) To login into superuser, go to *http://127.0.0.1:8000/admin* URL and an admin page will prompt up. Enter your admin info. You can see the

18) Enter the following code and into main/admin.py . Tutorial is a model created in main/models.py . Refresh the page and you will see Tutorials under group section in admin page. Our model name is Tutorial but its plural name is seen in groups of admin page because Django authomatically makes it plural.

```python
from .models import Tutorial
admin.site.register(Tutorial)
```

18) To use only a part of attributes in Model(Tutorial) in Admin page, use the Python code below. For example, if Tutorial model has 5 attributes and we want to use only 2 of them in the order we desire, the following should be written in main/admin.py

```python
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_content",
              "tutorial_published",
              "tutorial_title"
              ]

    fieldsets = [("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
    ("Content",{"fields":["tutorial_content"]})
    ]

admin.site.register(Tutorial,TutorialAdmin)
```

19) To group different attributes in main/admin.py

```python
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):


    fields = ["tutorial_content",
              "tutorial_published",
              "tutorial_title"
              ]

    fieldsets = [("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
    ("Content",{"fields":["tutorial_content"]})
    ]

admin.site.register(Tutorial,TutorialAdmin)
```

20) To assign a default value to tutorial_published attribute in main/models.py

```python
# Change tutorial_published = models.DateTimeField("date published") to
tutorial_published = models.DateTimeField("date published",default = timezone.now )

```

21) To run editing operations of admin via Control panel
    - Install the package tinymce4-lite  via **pip install django-tinymce4-lite**. tinymce4-lite is a django app.
    - Add 'tinymce' to **INSTALLED_APPS** list in **mysite/settings.py** file. 
    - Add the following text into  **mysite/settings.py**  
    ```
    TINYMCE_DEFAULT_CONFIG = {
        'height': 360,
        'width': 1120,
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 20,
        'selector': 'textarea',
        'theme': 'modern',
        'plugins': '''
                textcolor save link image media preview codesample contextmenu
                table code lists fullscreen  insertdatetime  nonbreaking
                contextmenu directionality searchreplace wordcount visualblocks
                visualchars code fullscreen autolink lists  charmap print  hr
                anchor pagebreak
                ''',
        'toolbar1': '''
                fullscreen preview bold italic underline | fontselect,
                fontsizeselect  | forecolor backcolor | alignleft alignright |
                aligncenter alignjustify | indent outdent | bullist numlist table |
                | link image media | codesample |
                ''',
        'toolbar2': '''
                visualblocks visualchars |
                charmap hr pagebreak nonbreaking anchor |  code |
                ''',
        'contextmenu': 'formats | link image',
        'menubar': True,
        'statusbar': True,
        }
    ```
    - Add **path('tinymce/',include('tinymce.urls')),** to urlpatterns in mysite/urls.py

    - Add the following lines to main/admin.py

    ```python
    from tinymce.widgets import TinyMCE
    from django.db import models

    # Under TutorialAdmin class
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

    ```

    - Refresh the admin page and add a new tutorial

22)




