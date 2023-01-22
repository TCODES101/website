from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('user', views.user, name='user'),
    path('history', views.history, name='history'),
    path('complete', views.complete, name='complete'),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="myapp/templates/reset_password.html"),
    name='reset_password'),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="myapp/templates/password_sent.html"),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="myapp/templates/password_complete.html"),
    name='password_reset_confirm'),

    path('reset_password_complete', 
    auth_views.PasswordResetCompleteView.as_view(template_name="myapp/templates/reset_done.html"), 
    name='password_reset_complete'),
]
