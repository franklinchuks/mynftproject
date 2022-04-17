from django.urls import path
from admin_dashboard.views import (
    admin_dashboard_view,
    nft_view,
    transaction_view,
    withdrawal_view,
)

app_name = 'admin_dashboard'

urlpatterns = [
    path('admin_dashboard/', admin_dashboard_view, name="admin_dashboard"),
    path('nft/', nft_view, name="nft"),
    path('transaction/', transaction_view, name="transaction"),
    path('withdrawal/', withdrawal_view, name="withdrawal"),
]
