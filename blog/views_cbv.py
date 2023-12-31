from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView

from .models import Blog
from .mixins import Base
from .forms import CommentForm, BlogForm
from django_filters.views import FilterView
from .filters import BlogFilter


class BlogListView(Base, FilterView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    filterset_class = BlogFilter

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     search = self.request.GET.get("search")
    #     if search is not None:
    #         return qs.filter(title__icontains=search)
    #     return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['test'] = 'test xabar'
        return context


# class BlogDetailView(Base, View):
#     template_name = 'blog/blog_detail.html'
#
#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         form = CommentForm()
#         context = {
#             'blog': blog,
#             'form': form,
#             'categories': self.category(),
#             'tags': self.tag()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request, pk):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = self.get_object(pk)
#             comment.user = request.user
#             comment.save()
#             return redirect('blog:blog_detail', pk)
#
#     def get_object(self, pk):
#         return get_object_or_404(Base, pk)

class BlogDetailView(Base, FormMixin, DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'
    form_class = CommentForm


    def get_object(self,queryset=None):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'Blog Detail Page'
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

    def success(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blog = self.get_object()
        comment.save()
        return super().form_valid(form)


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:home")
    template_name = 'blog/blog_create.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        return super().form_valid(form)
