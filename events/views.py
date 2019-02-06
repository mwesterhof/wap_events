from django.views.generic import DetailView
from rest_framework import viewsets

from .models import Event
from .serializers import CommentSerializer


class EventDetail(DetailView):
    model = Event

    def get_object(self, *args, **kwargs):
        return self.parent_page.event


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.request.parent_page.event.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            event=self.request.parent_page.event
        )
