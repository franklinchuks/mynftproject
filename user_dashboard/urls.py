from django.urls import path
from user_dashboard.views import(
    dashboard_view,
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    user_collections_view,
)

app_name = 'user_dashboard'

urlpatterns = [
    path('dashboard/', dashboard_view, name="dashboard"),
    path('create/', create_blog_view, name="create"),
    path('user_collections/', user_collections_view, name="user_collections"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
]
