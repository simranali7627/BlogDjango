from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView, CreateView, UpdateView
# Create your views here.
# class based views-> list, create , update etc

#home -> handle navigations from home

# posts = [
#     {
#         'author' : 'Simran Ali', 
#         'title' : 'Post 1', 
#         'content' : 'My first post',
#         'date_posted' : 'February 8, 2024'
#     },
#     {
#         'author' : 'Fakhra Najm', 
#         'title' : 'Post 2', 
#         'content' : 'My Second post',
#         'date_posted' : 'August 28, 2023'
#     },
#     {
#         'author' : 'Saif Ali', 
#         'title' : 'Post 3', 
#         'content' : 'My third post',
#         'date_posted' : 'September 12, 2023'
#     }
# ]


def home(request):
    # return HttpResponse('<h1>Blog home</h1>')
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1>Blog About page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

