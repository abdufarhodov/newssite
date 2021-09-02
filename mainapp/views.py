from rest_framework import serializers
from mainapp.models import Article,Category
from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializer import ArticleSerializer,CategorySerializer
from rest_framework.response import Response
from .paginations import DeafultLimitOffsetPagination

class ArticleViewGet(APIView):

    def get(self,request):
        paginator = DeafultLimitOffsetPagination()
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects,many = True)
        return paginator.generate_response(objects,ArticleSerializer,request)

    def post(self,request):
        serializer = ArticleSerializer(many = False,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')


class ArticleGet(APIView):

    def get(self,request,pk):
        objects = Article.objects.get(id=pk)
        serializer = ArticleSerializer(objects,many = False)
        return Response(serializer.data)

    def put(self,request,pk):
        objects = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=objects,data=request.data,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')
        
    def patch(self,request,pk):
        objects = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=objects,data=request.data,many = False,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')

    def delete(self,request,pk):
        Article.objects.get(id=pk).delete()
        return Response('Successfully deleted!')


class CategoryViewGet(APIView):

    def get(self,request):
        objects = Category.objects.all()
        serializer = CategorySerializer(objects,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(instance=objects,data=request.data,many = False)
        if serializer.is_valid():
            serializer.save()
        serializer = CategorySerializer(data=request.data,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')

class CategoryGet(APIView):
    
    def get(self,request,pk):
        objects = Category.objects.get(id=pk)
        serializer = CategorySerializer(objects,many = False)
        return Response(serializer.data)

    def put(self,request,pk):
        objects = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=objects,data=request.data,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')

    def patch(self,request,pk):
        objects = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=objects,data=request.data,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('XATO')

    def delete(self,request,pk):
        Category.objects.get(id=pk).delete()
        return Response("Successfully deleted!")


