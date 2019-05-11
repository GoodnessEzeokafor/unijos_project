from django.views import generic
from . models import Posts
from django.shortcuts import render, get_object_or_404

# Create your views here.

class PostList(generic.ListView):
    model = Posts
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'

def index(request):
    return render(request, PostList, PostDetail)
