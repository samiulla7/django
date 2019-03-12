from django.urls import path,include,re_path
from . import views
urlpatterns = [
    # re_path(r'^$', views.hello, name="hello"),
    path('', views.post_list, name='post_list'),
    path('dynamic_list/', views.post_list_dynamic, name='post_list_dynamic'),
]