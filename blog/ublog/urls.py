from django.urls import path
from .views import Main, Login, Logout, Register, Blog, Edit, DeletePost

urlpatterns = [
    path('', Main.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('blog', Blog.as_view(), name='blog'),
    path('edit/<int:pk>', Edit.as_view(), name='edit'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
]

