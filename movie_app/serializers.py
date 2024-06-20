from rest_framework import serializers
from .models import Movie, Director, Review, Stars
from rest_framework.exceptions import ValidationError

class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()

    def get_movies_count(self, obj):
        return obj.movie_set.count()


class ReviewSerializer(serializers.ModelSerializer):
    stars = StarsSerializer()
    # rating = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'stars text movie'.split()


class MoviesSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'rating reviews title description duration director'.split()

    def get_reviews(self, obj):
        return Review.objects.filter(movie=obj)

    def get_rating(self, obj):
        reviews = self.get_reviews(obj)
        if reviews.exists():
            return sum(review.stars.star for review in reviews) / reviews.count()
        return 0


class DirectorsValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)


class ReviewsValidateSerializer(serializers.Serializer):
    stars_id = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('movie not found!')
        return movie_id

    def validate_stars_id(self, stars_id):
        try:
            Stars.objects.get(id=stars_id)
        except Stars.DoesNotExist:
            raise ValidationError('wrong number!')
        return stars_id


class MoviesValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField(min_value=1)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('director not found!')
        return director_id
