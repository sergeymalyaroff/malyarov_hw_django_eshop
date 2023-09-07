from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/form.html', {'form': form})

def blog_update(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/form.html', {'form': form})

def blog_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/confirm_delete.html', {'post': post})


# величение счетчика просмотров при открытии статьи

from django.shortcuts import get_object_or_404

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj



# Вывод только опубликованных статей
class PostListView(ListView):
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

# Динамическое формирование slug name для заголовка

from slugify import slugify

class PostCreateView(CreateView):
    model = Post
    template_name = 'form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

# Перенаправление после редактирования

from django.urls import reverse

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('post_detail', args=[str(self.object.id)])
