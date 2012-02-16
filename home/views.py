# Create your views here.
from sitepass.views import menu
from articles.views import display_blog_page
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')
