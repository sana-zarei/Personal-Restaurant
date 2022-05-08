from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Restaurant.models import Profile,Contact

contact = Contact.objects.latest('updated')
profile = Profile.objects.all()

app_name = "Accounts"
urlpatterns = [
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.registerview, name='register'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name = "password_reset.html",extra_context={"profile":profile,'contact':contact,}), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html",extra_context={"profile":profile,'contact':contact,}), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html",extra_context={"profile":profile,'contact':contact,}), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html",extra_context={"profile":profile,'contact':contact,}), name='password_reset_complete'),
]