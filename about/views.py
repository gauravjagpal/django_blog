from django.shortcuts import render
from .models import About
##from .models import Post


# Create your views here.
def about(request):
    """
    Display an individual about me info
    about Gaurav Jagpal
    """
    
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )

