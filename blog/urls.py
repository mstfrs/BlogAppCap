from django.urls import path, include
from .views import PostListView


urlpatterns = [

    # path('auth/', include('dj_rest_auth.urls')),
    path('', PostListView.as_view()),

]
