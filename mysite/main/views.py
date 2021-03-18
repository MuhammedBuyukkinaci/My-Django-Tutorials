from django.shortcuts import render

from django.http import HttpResponse

from .models import Tutorial

from .models import TutorialCategory, TutorialSeries

#from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages

def single_slug(request, single_slug):
    print(single_slug)
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        print(matching_series.all())
        series_urls ={}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        #return HttpResponse("{} is a category !!".format(single_slug))
        return render(request,"main/category.html",{"part_ones":series_urls})
    
    
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorial_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series = this_tutorial.tutorial_series ).order_by("tutorial_published")

        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)

        return render(request,"main/tutorial.html",{"tutorial":this_tutorial,\
            "sidebar":tutorial_from_series,\
                "this_tutorial_idx":this_tutorial_idx})


        #return HttpResponse("{} is a tutorial !!".format(single_slug))
    
    return HttpResponse("{} doesn't correspond to any thing.".format(single_slug))



# Create your views here.

def homepage(request):
    # HTML can be below as a parameter to HttpResponse
    #return HttpResponse("This is a <strong> NEW </strong> tutorial")
    
    #return render( request = request,template_name = "main/home.html",context = {"tutorials": Tutorial.objects.all} )

    return render( request = request,template_name = "main/categories.html",context = {"categories": TutorialCategory.objects.all} )


# def register(request):

#     form = UserCreationForm()
#     return render(request,
#                 template_name = "main/register.html",
#                 context={"form": form})

def register(request):

    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"New Account Created {}".format(username))
            login(request,user)
            messages.info(request,"You are now logged in as {}".format(username))
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error( request, "{}:{}".format(msg,form.error_messages[msg]) )

    #form = UserCreationForm
    form = NewUserForm
    return render(request,
                template_name = "main/register.html",
                context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect("main:homepage")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Don't forget to use username= and password= phrases.
            user = authenticate(username = username,password= password)
            if user is not None:
                login(request,user)
                messages.info(request,"You are now logged in as {}".format(username))
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,"main/login.html",{"form": form})
