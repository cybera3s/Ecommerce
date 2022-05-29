from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import authentication
from rest_framework import permissions


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


