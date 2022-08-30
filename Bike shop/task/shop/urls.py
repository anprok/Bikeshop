from django.urls import path
from .views import BikeListView, BikeDetailView, OrderDetailView


urlpatterns = [
    path('bikes/', BikeListView.as_view()),
    path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
