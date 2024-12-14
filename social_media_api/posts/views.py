from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post , Comment
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def get_queryset(self):
        queryset= super().get_queryset()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)|
                Q(content__icontains=search_query)

            )
            return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
