
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

blog_posts = {
    "gardening_tools": "blog post about gardening tools",
    "soil_amendments": "add these things to your soil: lime, gypsum, organic matter"
}

def home_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")

def post_detail(request, slug):
    pass