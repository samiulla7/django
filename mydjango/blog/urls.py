from django.urls import path,include,re_path
from . import views
urlpatterns = [
    # re_path(r'^$', views.hello, name="hello"),
    path('static_list', views.post_list, name='post_list'),
    path('', views.post_list_dynamic, name='post_list_dynamic'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('registration/', views.registration, name='registration'),
]