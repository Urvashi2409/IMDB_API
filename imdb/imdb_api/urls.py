from django.urls import path, include
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream', views.StreamPlatformViewSet, basename="streamplatform")
router.register(r'list', views.WatchListViewSet, basename="watchlist")

# name = streamplatform-detail hi rkhna 
urlpatterns = [
    path('', include(router.urls)),
    path('list/<int:pk>/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('list/<int:pk>/review-create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('list/reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('', views.api_root),
]

# urlpatterns = format_suffix_patterns(urlpatterns)