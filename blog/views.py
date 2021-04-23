from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post/list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.order_by('pk').all()
        return context

    def get_queryset(self):
        # object_list = Post.objects.filter(user=self.request.user).order_by('post.id').all()
        object_list = Post.objects.all()
        return object_list
