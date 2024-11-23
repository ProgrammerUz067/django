from django.shortcuts import render
from rest_framework.generics import ListAPIView,DestroyAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer,CategorySerializers
from .models import Article,Category
from rest_framework.viewsets import ModelViewSet

# class ArticleView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArticleView(APIView):
    def get(self,request):
        articles=Article.objects.all()
        serializers=ArticleSerializer(articles,many=True).data
        data={
            "status":True,
            "massage":"qonday",
            "articles":serializers
        }
        return Response(data)


# class ArcitleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArcitleDeleteView(APIView):
    def delet(self,request,pk):
        article=Article.objects.get(id=pk)
        article.delete()
        data={
            "status":True,
            "message":"Yangilik muofaqiyatli o'chiridi",
        }
        return Response(data)


class CreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleUptateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




class CategoryView(APIView):
    def get(self, request):
        articles = Category.objects.all()
        serializers = CategorySerializers(articles, many=True).data
        data = {
            "status": True,
            "massage": "qonday",
            "articles": serializers,
        }
        return Response(data)


class CategoryDeletView(APIView):
        def delet(self, request, pk):
            category = Category.objects.get(id=pk)
            Category.delete()
            data = {
                "status": True,
                "message": "Categoriya muofaqiyatli o'chiridi",
            }
            return Response(data)



class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers




class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer





