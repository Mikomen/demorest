from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'id']

class UserCreatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class ArticleCreateSerializer(serializers.ModelSerializer):
    author = UserCreatSerializer()

    class Meta:
        model = Article
        fields = ['title', 'desc', 'author', 'created']

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ['title', 'desc', 'author', 'created']

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('author')
    #     article = Article.objects.create(**validated_data)
    #     for author_data in authors_data:
    #         Article.objects.create(article=article, **author_data)
    #     return article



