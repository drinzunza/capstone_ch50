from django.urls import path
from .views import ListPostsView, CreatePostView, PostDetailsView, UpdatePostView, DeletePostView

urlpatterns = [
    path('list/', ListPostsView.as_view(), name="list_posts"),
    path('create/', CreatePostView.as_view(), name="create_post"),
    path('details/<int:pk>/', PostDetailsView.as_view(), name="details_post"),
    path('update/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('delete/<int:pk>/', DeletePostView.as_view(), name="delete_post"),
]
