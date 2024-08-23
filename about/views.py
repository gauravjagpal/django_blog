from django.shortcuts import render, get_object_or_404
from django.views import generic
##from .models import Post


# Create your views here.
def about(request):
    """
    Display an individual about me info
    about Gaurav Jagpal
    """
    
    return render(
        request,
        "about/about.html",
        {"about": about}
    )

