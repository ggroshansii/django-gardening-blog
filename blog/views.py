from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

blog_posts = {
    "gardening_tools": "blog post about gardening tools",
    "soil_amendments": "add these things to your soil: lime, gypsum, organic matter"
}

def index(request):
    return HttpResponse("homepage")

def posts(request):
    return HttpResponse("all posts")

def post_detail(request, post_detail):
    return HttpResponse(blog_posts[post_detail])