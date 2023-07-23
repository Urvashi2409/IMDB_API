from django.urls import path, include
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream', views.StreamPlatformViewSet, basename="streamplatform")
router.register(r'list', views.WatchListViewSet, basename="watchlist")

# name = streamplatform-detail hi rkhna 
urlpatterns = [
    # path('list/', views.movie_list, name='watchlist-list'),
    # path('list/<int:pk>', views.movie_detail, name='watchlist-detail'),
    path('', include(router.urls)),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    # path('stream/', streamplatform_list, name='streamplatform-list'),
    # path('stream/<int:pk>', streamplatform_detail, name='streamplatform-detail'),
    path('', views.api_root),
]

# urlpatterns = format_suffix_patterns(urlpatterns)