from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer,ArticleSerializer,ArticleCreateSerializer
from .models import Article
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]






class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        self.serializer_class = ArticleCreateSerializer(data=request.data)
        if self.serializer_class.is_valid():
            self.serializer_class.save()
        super().create(self, request)
        return Response(serializer.data)
        # super().create(self, request)
        # return response.Response(status=status.HTTP_201_CREATED)

    # def create(self, request):
    #     serializer = ArticleCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     super().create(self, request)
    #     return Response(serializer.data)

    # def create(self, request):
    #     self.serializer_class = ArticleCreateSerializer(data=request.data)
    #     super().create(self, request, *args, **kwargs)
    #     return response.Response(status=status.HTTP_201_CREATED)

    # def create(self, request, serializer):
    #     serializer.save(user=self.request.user)
    #     self.serializer_class = ArticleCreateSerializer(data=request.data)
    #     super().create(self, request, *args, **kwargs)
    #     return Response(serializer.data)

    def update(self, request, pk=None):
        self.serializer_class = ArticleCreateSerializer(data=request.data)
        return super().update(self, request)

    # def list(self, request):
    #     self.serializer_class = ArticleSerializer
    #
    # def retrieve(self, request, pk=None):
    #     self.serializer_class = ArticleSerializer




class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



# class UserViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         pass
#
#     def create(self, request):
#         self.ArticleViewSet
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass