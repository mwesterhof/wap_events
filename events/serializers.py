from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)

    def validate(self, data):
        return data

    class Meta:
        model = Comment
        fields = ['pk', 'message', 'username']
        read_only_fields = ['username']
