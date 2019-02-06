from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        return data

    class Meta:
        model = Comment
        fields = ['pk', 'message']

    def to_internal_value(self, data):
        return dict(
            user=self.context['user'],
            event=self.context['event'],
            message=data['message']
        )

    def to_representation(self, instance):
        return {
            'pk': instance.pk,
            'username': instance.user.username,
            'message': instance.message
        }
