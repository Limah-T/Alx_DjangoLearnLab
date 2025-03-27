from django.urls import path
from . import views

urlpatterns = [
# """Post API Endpoints"""
    path('post/create', views.CreateView.as_view()),
    path('posts', views.ListView.as_view()),
    path('post/<int:id>', views.RetrieveView.as_view()),
    path('post/<int:id>/update', views.UpdateView.as_view()),
    path('post/<int:id>/delete', views.DeleteView.as_view()),

#   """Comment API Endpoints"""
    path('comment/create', views.CommentCreateView.as_view()),
    path('comments', views.CommentListView.as_view()),
    path('comment/<int:id>', views.CommentRetrieveView.as_view()),
    path('comment/<int:id>/update', views.CommentUpdateView.as_view()),
    path('comment/<int:id>/delete', views.CommentDeleteView.as_view()),
]