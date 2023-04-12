from django.urls import path

from .views import BlogListView, add_comment_to_post

urlpatterns = [
    path('post/<int:pk>/', add_comment_to_post, name='post_detail'),
##    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('', BlogListView.as_view(), name='home'),
]
