from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, EventDetail


router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('', EventDetail.as_view(), name='event_detail'),
    path('api/', include(router.urls)),
]
