from django.urls import path
from . import views

app_name = "Blog"
urlpatterns = [
    path('blog/', views.home, name='blog'),
    path('blog/<int:page>/', views.home, name='pageblog'),
    path('blog/<slug:slug>/', views.detail, name='blogdetails'),
    path('blog/category/<slug:slug>/', views.category, name='category'),
    path('blog/category/<slug:slug>/page/<int:page>', views.category, name='category2'),
]