from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, ReviewSerializer, MoviesSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def directors_list_api_view(request):

    data = Director.objects.all()
    list_ = DirectorSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def movies_list_api_view(request):

    data = Movie.objects.all()
    list_ = MoviesSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def review_list_api_view(request):

    data = Review.objects.all()
    list_ = ReviewSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def directors_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=404)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=404)
    data = MoviesSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=404)
    data = ReviewSerializer(reviews).data
    return Response(data=data)