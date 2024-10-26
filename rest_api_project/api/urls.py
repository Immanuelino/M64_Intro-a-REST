from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view()),  # GET (list), POST (create)
    path('users/<int:user_id>/', UserAPIView.as_view()),  # GET (detail), PUT (update), DELETE (delete)
]
