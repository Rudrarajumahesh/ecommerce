from django.urls import path
from .views import ProductListCreateView, UserDetailView

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
]