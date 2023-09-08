from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from slugify import slugify
from django.urls import reverse_lazy
from django.views.generic import DeleteView




class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj

class PostListView(ListView):
    model = BlogPost
    template_name = 'post_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class PostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('post_detail', args=[str(self.object.id)])

def post_list_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})



class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')