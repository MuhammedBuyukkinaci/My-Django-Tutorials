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

## Views and Templates

22) Change return part of main/views.py to the code below. *tutorials* is a variable which is ready to be called in main/templates/main/home.html :

```python

# Former code:
def homepage(request):
    return HttpResponse("This is a <strong> NEW </strong> tutorial")

# New code:
from .models import Tutorial
def homepage(request):    
    return render( request = request, 
        template_name = "main/home.html", 
        context = {"tutorials": Tutorial.objects.all} )

```

23) Create 2 folders whose directories are main/templates and main/templates/main. Put your relevant html files under main/templates/main directory. Fill html files using materialize.css framework and JS.

## Styling with CSS

24) Materialize is a framework to deal with CSS

25) Copy the code below to an html file to usee materialize css

```html
<!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
            
```

26) extends and include properties of Django correspond to Layout in ASP.NET Core. extends is like _Layout.cshtml file. An extentds usage is below in main/templates/main/home.html like this in the beginning of HTML file: 

```html
{% extends "main/header.html" %}
```

27) Copy main/templates/main/home.html and name it as *header.html*. *header.html* includes the components in html which is common among many html files. It reduces the code we write as we did in ASP.NET Core. You should remove all components which exist in *header.html* from *home.html*.

28) Create a folder of main/static/main/css and put your css files in this folder. 

## User Registration

29) To look at user models, prompt up an interactive shell

```python
from django.contrib.auth.models import User
dir(User)
```

30) Copy *home.html* and name it as *register.html*.

31) In Django, forms are based on Django, not based on HTML.

32) Add the following lines to *main/views.py* and add *path("/register", views.register, name = "register"),* to *urlpatterns* list in *main/urls.py* to be activated. The below *register* function is a GET method and the client only GETs the information in the page. However, in order to POST a submit,

```python
# redirect means directing the user to a page.
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                template_name = "main/register.html",
                context={"form": form})

```

33) To use a variable which was sent from a views.py file to an html file, the sent variable should be double-curly-paranthesized like this {{VARIABLE_SENT_TO_HTML}} like {{form}} or {{tutorials}}

34) {{form.as_p}}, {{form.as_ul}} and {{form.as_table}} can be used in register.html instead of {{form}} to have a better UX.

## Messages and Includes

35) After registering, we should pop up something like "new account created". TO do this, add the following lines to  **main/views.py**

```python
from django.contrib import messages

def register(request):
    username = form.cleaned_data.get('username')
    messages.success(request,"New Account Created {}".format(username))

```

36) To add pop-up messages, we added the below code to messages.html.

```html
{% if messages %}
        {% for message in messages %}
            {% if message.tags == 'success'%}
                <script>M.toast({html: "{{message}}", classes: 'green rounded', displayLength:2000});</script>
            {% elif message.tags == 'info'%}
                <script>M.toast({html: "{{message}}", classes: 'blue rounded', displayLength:2000});</script>
            {% elif message.tags == 'warning'%}
                <script>M.toast({html: "{{message}}", classes: 'orange rounded', displayLength:10000});</script>
            {% elif message.tags == 'error'%}
                <script>M.toast({html: "{{message}}", classes: 'red rounded', displayLength:10000});</script>
            {% endif %}
        {% endfor %}
{% endif %}
```

37) **includes** is a property similar to Partial View property of ASP.NET Core. It only contains a partial html code and it was called by a different HTML file. To use **includes**, create a folder named includes in main/templates/main/ and put your HTML file (*navbar.html*) in it. Put the navbar content written in header.html to *navbar.html*. Then, call the content of *navbar.html* file in *header.html* via

```html
{% include "main/includes/navbar.html" %}
```

## Logout && Login

38) urls point to views.py and views.py points to templates.

39) `from django.contrib.auth.forms import UserCreationForm` is used for registry operations and `from django.contrib.auth.forms import AuthenticationForm` is used for log-in operations in *views.py*.

40) For login and logut operations, look at login_request and logout request functions in *views.py*

41) Copy *main/views.py* and rename it as *forms.py* to create a custom form instead of UserCreationForm in *main/views.py* . 

## Linking models with foreign keys

42) The purpose of foreign key is to bind DB tables which are related to each other.

43) Create 2 new models named as TutorialCategory and TutorialSeries in *main/models.py* and then makemigrations and migrate.

44) Add these 2 lines to Tutorial class in *main/models.py*.

```python
tutorial_series = models.ForeignKey(TutorialSeries,default=1,verbose_name="Series",on_delete = models.SET_DEFAULT)
tutorial_slug = models.CharField(max_length=200,default=1)
```

45)  Add 2 attributes to admin.py via this code: 

```python
("URL",{"fields":["tutorial_slug"]}),
("Series",{"fields":["tutorial_series"]}),
```

46) Go to Add Tutorial page via and then add Series and Categories and Tutorials on *http://127.0.0.1:8000/admin*

## Working with Foreign Keys

47) Contact & Registration pages are usually single-slug.

48) We should first determine whether it(uRL) is category or specific tutorial.

49) Category maps to Series. Series map to Tutorials.

50) Move to *main/views.py*. Add single_slug method and update homepage function by looping over categories rather than tutorials on main/templates/main/categories.html.

51) Add this line to main/urls.py. *"<single_slug>"* is a variable passed to views.single_slug

```python
path("<single_slug>",views.single_slug,name="single_slug"),
```

52) Create category.html via copying categories.html and change its content by copying from [here](https://pythonprogramming.net/working-foreign-keys-django-tutorial/).

53) In *main/models.py*, the return of def *__str__(self)* is used to bind different models. Its return value is the attribute to bind it to other tables(models)

54) Fill single_slug function in *main/views.py*.

55) In main/views.py, TutorialSeries has a Foreign Key (FK) on its tutorial_category attribute. This FK makes TutorialSeries access to TutorialCategory and merge with TutorialCategory. category_slug is an attribute of TutorialCategory. The category_slug which is equal to single_slug is filtered on the below code.



```python
#TutorialSeries has a FK on tutorial_category attribute, which maps to TutorialCategory's category_slug attribute
# tutorial_category is FK of TutorialSeries
# category_slug is the column linked via FK on TutorialCategory table(model) 
matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
```

## Dynamic Sidebar

56) Tutorial.objects.filter return list and Tutorial.objects.get a single object.

57) Create tutorial.html in main/templates/main/

58) In HTML files for Django, forloop.counter0 start from 1, not from 0.

59) The below code in header.html is used to activate JS properties of Materialize CSS.

```html
<script>M.AutoInit();</script>
```












