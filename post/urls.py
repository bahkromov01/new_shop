from django.urls import path
from post.views import PostApiView, PostModelViewSet, PostDetailApiView
urlpatterns = [
    path('post-list/', PostApiView.as_view()),
    path('post-actions/', PostModelViewSet.as_view()),
    path('post-detail/<int:pk>/', PostDetailApiView.as_view())
]