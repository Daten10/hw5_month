from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (DirectorSerializer, ReviewSerializer, MoviesSerializer, DirectorsValidateSerializer,
                          MoviesValidateSerializer, ReviewsValidateSerializer)
from .models import Director, Movie, Review

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def post(self, request, *args, **kwargs):
                serializer = DirectorsValidateSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

                name = serializer.validated_data.get('name')
                director = Director.objects.create(
                    name=name
                )
                return Response(data={'director_id': director.id, 'name': director.name}, status=status.HTTP_201_CREATED)


class DirectorItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
            serializer = MoviesValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            duration = serializer.validated_data.get('duration')
            director_id = serializer.validated_data.get('director_id')

            movie = Movie.objects.create(
                title=title,
                description=description,
                duration=duration,
                director_id=director_id
            )
            return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description,
                                  'duration': movie.duration, 'director_id': movie.director_id},
                            status=status.HTTP_201_CREATED)


class MovieItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = 'id'


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
                serializer = ReviewsValidateSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

                stars_id = serializer.validated_data.get('stars_id')
                text = serializer.validated_data.get('text')
                movie_id = serializer.validated_data.get('movie_id')

                review = Review.objects.create(
                    stars_id=stars_id,
                    text=text,
                    movie_id=movie_id
                )
                return Response(data={'stars_id': review.stars_id, 'text': review.text, 'movie_id': review.movie_id},
                                status=status.HTTP_201_CREATED)


class ReviewItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

#
# @api_view(['GET', 'POST'])
# def directors_list_api_view(request):
#     print(request.user)
#     if request.method == 'GET':
#         data = Director.objects.all()
#         list_ = DirectorSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#
#         serializer = DirectorsValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         name = serializer.validated_data.get('name')
#         director = Director.objects.create(
#             name=name
#         )
#         return Response(data={'director_id': director.id, 'name': director.name}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'POST'])
# def movies_list_api_view(request):
#     if request.method == 'GET':
#         data = Movie.objects.all()
#         list_ = MoviesSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#
#         serializer = MoviesValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director_id = serializer.validated_data.get('director_id')
#
#         movie = Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director_id=director_id
#         )
#         return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description,
#                               'duration': movie.duration, 'director_id': movie.director_id},
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         data = Movie.objects.all()
#         list_ = MoviesSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#
#         serializer = ReviewsValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         stars_id = serializer.validated_data.get('stars_id')
#         text = serializer.validated_data.get('text')
#         movie_id = serializer.validated_data.get('movie_id')
#
#         review = Review.objects.create(
#             stars_id=stars_id,
#             text=text,
#             movie_id=movie_id
#         )
#         return Response(data={'stars_id': review.stars_id, 'text': review.text, 'movie_id': review.movie_id},
#                         status=status.HTTP_201_CREATED)

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def directors_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Not found'}, status=404)
#
#     if request.method == 'GET':
#         data = DirectorSerializer(director).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = DirectorsValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         director.name = serializer.validated_data.get('name')
#         director.save()
#         return Response(status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movies_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Not found'}, status=404)
#
#     if request.method == 'GET':
#         data = MoviesSerializer(movie).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#
#         serializer = MoviesValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.director_id = serializer.validated_data.get('director_id')
#
#         movie.save()
#         return Response(status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def reviews_detail_api_view(request, id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Not found'}, status=404)
#
#     if request.method == 'GET':
#         data = ReviewSerializer(reviews).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#
#         serializer = ReviewsValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#         reviews.stars_id = serializer.validated_data.get('stars_id')
#         reviews.text = serializer.validated_data.get('text')
#         reviews.movie_id = serializer.validated_data.get('movie_id')
#         reviews.save()
#         return Response(status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
