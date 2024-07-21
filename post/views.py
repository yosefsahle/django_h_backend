from rest_framework import generics
from .models import Post, Comment
from .serializer import PostSerializer, PostCreateSerializer, CommentSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,BasePermission

class IsPostCreator(BasePermission):
    allowed_roles = {'FPM', 'NPM', 'PM', 'A', 'SA'}

    def has_permission(self, request, view):
        if request.method == 'POST':
            user = request.user
            return user.role in self.allowed_roles
        return True
    

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated, IsPostCreator]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]