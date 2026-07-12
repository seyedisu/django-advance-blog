from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class PostList(ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         post.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def destroy(self, request, pk):
#         post = get_object_or_404(self.queryset, pk=pk)
#         post.delete()
#         return Response({"detail":"item removed successfully."}, status=status.HTTP_204_NO_CONTENT)

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

