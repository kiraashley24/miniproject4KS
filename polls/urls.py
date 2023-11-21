from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view
from .views import index

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name="register"),
    path('showtimes/', views.showtimes, name='showtimes'),
    path('menu/', views.menu, name='menu'),
    path('tickets/', views.tickets, name='tickets'),
    path("contact/", views.contact, name="contact"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
