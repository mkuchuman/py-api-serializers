from django.urls import include, path
from rest_framework import routers

from cinema.views import (CinemaHallViewSet,
                          ActorViewSet,
                          GenreViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

router = routers.SimpleRouter()
router.register("cinema_halls",
                CinemaHallViewSet, basename="cinema_halls")
router.register("actors",
                ActorViewSet, basename="actors")
router.register("genres",
                GenreViewSet, basename="genres")
router.register("movies",
                MovieViewSet, basename="movies")
router.register("movie_sessions",
                MovieSessionViewSet, basename="movie_sessions")


urlpatterns = router.urls

app_name = "cinema"
