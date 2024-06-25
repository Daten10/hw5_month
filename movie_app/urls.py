from django.urls import path
from . import views


urlpatterns = [
    path('', views.directors_list_api_view),
    path('<int:id>/', views.directors_detail_api_view),
    path('', views.movies_list_api_view),
    path('<int:id>/', views.movies_detail_api_view),
    path('', views.review_list_api_view),
    path('<int:id>/', views.reviews_detail_api_view)
]