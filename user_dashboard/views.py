from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from user_dashboard.forms import AccountAuthenticationForm, RegistrationForm, AccountUpdateForm
from user_dashboard.models import BlogPost, Account
from user_dashboard.forms import CreateBlogPostForm
from user_dashboard.forms import UpdateBlogPostForm


# Create your views here.

# REGISTRATION FORM
def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user_dashboard/register.html', context)

# LOGOUT FORM


def logout_view(request):
    logout(request)
    return redirect('home')

# LOGIN FORM


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user_dashboard/login.html', context)

# EDIT EMAIL AND USERNAME


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )

    context['account_form'] = form

    # QUERYING BLOG POSTS
    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts
    # END OF QUERYING BLOG POSTS

    return render(request, 'user_dashboard/account.html', context)

# USER MAIN DASHBOARD VIEW


def dashboard_view(request):
    return render(request, 'user_dashboard/dashboard.html')

# FORM TO CREATE BLOG


def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form
    return render(request, "user_dashboard/create_blog.html", context)

# MUST AUTHENTICATE VIEW


def must_authenticate_view(request):
    return render(request, 'user_dashboard/must_authenticate.html', {})


def detail_blog_view(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'user_dashboard/detail_blog.html', context)


def edit_blog_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(
            request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated successfully"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={"title": blog_post.title, "body": blog_post.body, "image": blog_post.image})

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    context['form'] = form
    context['blog_post'] = blog_post

    return render(request, "user_dashboard/edit_blog.html", context)


# QUERYING User BLOG POSTS
def user_collections_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, 'user_dashboard/user_collections.html', context)
