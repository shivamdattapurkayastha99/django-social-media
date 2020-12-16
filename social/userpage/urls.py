from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome,name='userhome'),
    path('post', views.post,name='post'),
    path('like', views.likepost,name='likepost'),
    path('<int:post_id>/', views.delPost,name='delPost'),
    path('<str:username>/', views.userProfile,name='userprofile'),
    path('slug/comment/', views.comment,name='comment'),
    # path("user/follow/<str:username>/", views.follow, name="follow"),
    path('search/', views.Search_User.as_view(),name='search_user'),
]