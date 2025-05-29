from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list_view, name='user_list'),
    path('follow/<int:user_to_follow_id>/', views.follow_view, name='follow_user'),
    path('unfollow/<int:user_to_unfollow_id>/', views.unfollow_view, name='unfollow_user'),
]
