from django.shortcuts import render
from operator import attrgetter
from user_dashboard.models import BlogPost

# Create your views here.


# QUERYING All BLOG POSTS

def home_view(request):

    context = {}

    all_blog_posts = sorted(BlogPost.objects.all(),
                            key=attrgetter('date_uploaded'), reverse=True)
    context['all_blog_posts'] = all_blog_posts

    return render(request, 'home_dashboard/home.html', context)
