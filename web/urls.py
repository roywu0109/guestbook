from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='message/')),
    path('message/', MessageListView.as_view()),
    path('message/<int:pk>/', MessageDetailView.as_view()),
    path('message/create/', MessageCreate.as_view()),
    path('message/<int:pk>/delete/', MessageDelete.as_view()),
]