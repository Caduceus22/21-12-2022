from django.urls import path

from .views import (
    HomePageView,
    TkpDetailView,
    TkpCreateView,
    TkpUpdateView,
    TkpDeleteView,
)


urlpatterns = [
    path('tkp/<int:pk>/delete/', TkpDeleteView.as_view(), name='tkp_delete'),
    path('tkp/<int:pk>/edit/', TkpUpdateView.as_view(), name='tkp_edit'),
    path('tkp/new/', TkpCreateView.as_view(), name='tkp_add'),
    path('tkp/<int:pk>/', TkpDetailView.as_view(), name='tkp_detail'),
    path('', HomePageView.as_view(), name='home'),
]
