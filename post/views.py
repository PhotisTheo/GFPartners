from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    latest = Post.objects.order_by('-timestamp')[0:2]
    context = {
        'latest': latest
    }
    return render(request, 'index.html', context)


def blog(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.order_by('-timestamp')
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,

    }
    return render(request, 'blog.html', context)


def post(request, id):
    most_recent = Post.objects.order_by('-timestamp')[:4]
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
        'most_recent': most_recent,
    }
    return render(request, 'post.html', context)
