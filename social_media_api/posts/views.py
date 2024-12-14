from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post , Comment , Like
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from django.http import JsonResponse

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
    
@login_required
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like , created = Like.objects.get_or_create(user=request.user, post=post)
    if created :
        Notification.objects.create(
            recipient = post.author,
            actor = request.user,
            target = post,
            verb = 'liked your post' )
        return JsonResponse({'status':'liked'})
    return JsonResponse({'status':'already liked'})

@login_required 
def unlike_post(request,pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return JsonResponse({'status':'unliked'})
    return JsonResponse({'status':'not liked'})
