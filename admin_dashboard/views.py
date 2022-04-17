from django.shortcuts import render, redirect
from user_dashboard.models import BlogPost, Account

# Create your views here.


def admin_dashboard_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'admin_dashboard/admin_dashboard.html', context)


# QUERYING BLOG POSTS for Admin and Other Users

def nft_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    blog_posts = BlogPost.objects.filter(author=request.user)
    other_blog_posts = BlogPost.objects.exclude(author=request.user)
    context = {
        'blog_posts': blog_posts,
        'other_blog_posts': other_blog_posts
    }

    context['blog_posts'] = blog_posts
    context['other_blog_posts'] = other_blog_posts
    return render(request, 'admin_dashboard/nft.html', context)


def transaction_view(request):
    return render(request, 'admin_dashboard/transaction.html')


def withdrawal_view(request):
    return render(request, 'admin_dashboard/withdrawal.html')
