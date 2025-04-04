from django.urls import path, include
from .views import (PostList, PostDetail)


app_name='blog_api'
urlpatterns = [
    path('<int:pk>/', 
            PostDetail.as_view(), 
            name=('detail_create'),
        ),
    path('', 
            PostList.as_view(), 
            name=('list_create'),
        ),
]