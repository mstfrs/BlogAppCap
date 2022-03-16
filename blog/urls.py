from django.urls import path, include
from .views import PostList, PostDetail, PostCreate


urlpatterns = [


    path('list/', PostCreate.as_view(), name="postlist"),
    path('list/<int:pk>/', PostDetail.as_view(), name="postdetail")

]
