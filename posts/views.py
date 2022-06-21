from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Category, Comment, About, ContactUs
# from .forms import CategoryForm



# Create your views here.
def post_list(request):
    all_posts = Post.objects.all().order_by('-date')
    latest_posts = Post.objects.order_by('-date')[:3]
    paginator = Paginator(all_posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    categories = Category.objects.all()

    if request.method == 'POST':
        query = request.POST.get('q', None)
        submit_button = request.POST.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(body__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            contexts = {
                'query': query,
                'results': results,
                'submit_button': submit_button
            }
            return render(request, 'posts/search_results.html', contexts)
    context = {
        'posts': posts,
        'categories': categories,
        'title': all_posts[0].title if all_posts else None,
        'id': all_posts[0].id if all_posts else None,
        'slug': all_posts[0].slug if all_posts else None,
        'latest_posts': latest_posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = post.comments.filter(active=True).order_by('-updated')
    latest_posts = Post.objects.order_by('-date')[:3]
    categories = Category.objects.all()

    if request.method == 'POST':
        body = request.POST['body']
        full_name = request.POST['full_name']
        email = request.POST['email']

        new_comment = Comment(
            name=full_name, email=email, post=post, comment=body
        )
        new_comment.save()
        return HttpResponseRedirect('/blog/')
    context = {
        'post': post,
        'comments': comments,
        'latest_posts': latest_posts,
        'categories': categories
    }
    return render(request, 'posts/post_details.html', context)


def post_category(request, category):
    latest_posts = Post.objects.order_by('-date')[:3]
    categories = Category.objects.all()
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "posts": posts,
        'latest_posts': latest_posts,
        'categories': categories

    }
    return render(request, "posts/post_category_list.html", context)



