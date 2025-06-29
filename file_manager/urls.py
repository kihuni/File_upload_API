from django.urls import path
from .views import FileUploadView, FileListView, FileRetrieveView, FileDeleteView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileRetrieveView.as_view(), name='file-retrieve'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),
]