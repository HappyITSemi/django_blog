import logging

from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post/list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.order_by('pk').all()

        # logger = logging.getLogger("django")
        # logger.debug("level-debug")
        # logger.info("level-info")
        # logger.warning("level-warning")
        # logger.error("level-error")

        return context

    def get_queryset(self):
        # object_list = Post.objects.filter(user=self.request.user).order_by('post.id').all()
        object_list = Post.objects.all()
        return object_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/create.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        # post.user = self.request.user  # Login-userをセットする
        # print(self.request.user)
        post.save()
        messages.success(self.request, 'Postを新規作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Postの新規作成に失敗しました。")
        return super().form_invalid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/update.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        # post.user = self.request.user  # Login-userをセットする
        # print(self.request.user)
        post.save()
        messages.success(self.request, 'PostのUpdateにしました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "PostのUpdateに失敗しました。")
        return super().form_invalid(form)


class PostDeleteView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/delete.html'
    success_url = reverse_lazy('blog:post_list')
