from django.urls import path
from .views.auth_view import RegisterView, LoginView, VerificationView, SellerVerificationView, LogoutView, SellerDashboardView
 

app_name = "users" 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-otp/', VerificationView.as_view(), name='verify_otp'),
    path('seller-verification/', SellerVerificationView.as_view(), name='seller_verification'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('seller/dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),


]
