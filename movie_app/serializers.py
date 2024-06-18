from rest_framework import serializers
from .models import Movie, Director, Review, Stars


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
    rating = serializers.SerializerMethodField()

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