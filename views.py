from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog_homepage(request):
    posts = Post.objects.all().order_by('-publication_date')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = category.post_set.all()
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blog/category_posts.html', context)
