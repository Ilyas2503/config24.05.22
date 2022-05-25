from django.urls import path

from .views import PostView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('api/v1/post/', PostView.as_view(), name='posts'),
    path('api/v1/post/', PostCreateView.as_view(), name='create_post'),
    path('api/v1/post/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('api/v1/post_update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
]
