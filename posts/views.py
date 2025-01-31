from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
# Create your views here.
class ListPostsView(ListView):
    template_name = "posts/list_posts.html"
    model = Post
    context_object_name = 'post_list'


class CreatePostView(CreateView):
    template_name = "posts/create_post.html"
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user # logged in user
        return super().form_valid(form) # continue with the process
    


class PostDetailsView(DetailView):
    template_name = "posts/details.html"
    model = Post


class UpdatePostView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('list_posts')
    

class DeletePostView(DeleteView):
    template_name = "posts/delete.html"
    model = Post

    def get_success_url(self) -> str:
        return reverse('list_posts')
    