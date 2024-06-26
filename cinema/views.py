# write views here
from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                MovieSerializer,
                                MovieSessionSerializer,
                                CinemaHallSerializer,
                                MovieListSerializers,
                                MovieRetrieveSerializer,
                                MovieSessionListSerializers,
                                MovieSessionRetrieveSerializer)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializers
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializers
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.select_related()
        return self.queryset
