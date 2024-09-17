
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.decorators import action
from .models import Song, Playlist, PlaylistSong
from .serializers import SongSerializer, PlaylistListSerializer, PlaylistDetailSerializer, PlaylistSongSerializer, PlaylistSongSerializer2
from django.db import models



class SongPagination(PageNumberPagination):
    page_size = 10

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    pagination_class = SongPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("The song entry has been created.", status=status.HTTP_201_CREATED, headers=headers)



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   




class PlaylistPagination(PageNumberPagination):
    page_size = 10

class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistListSerializer
    pagination_class = PlaylistPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        playlist = serializer.save()  # Move this line before accessing request.data
        headers = self.get_success_headers(serializer.data)
        songs = request.data.get('songs', [])

        for i, song_id in enumerate(songs, start=1):
            song = Song.objects.get(id=song_id)
            PlaylistSong.objects.create(playlist=playlist, song=song, position=i)

        return Response("The playlist entry has been created.", status=status.HTTP_201_CREATED, headers=headers)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



class PlaylistSongPagination(PageNumberPagination):
    page_size = 10

class PlaylistSongListView(generics.ListAPIView):
    serializer_class = PlaylistSongSerializer
    pagination_class = PlaylistSongPagination

    def get_queryset(self):
        playlist_id = self.kwargs['playlist_id']
        playlist = Playlist.objects.get(id=playlist_id)
        return playlist.playlistsong_set.order_by('position')


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



class PlaylistSongUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer2
    lookup_url_kwarg = 'song_id'
    lookup_fields = ['playlist__id', 'song__id']


    def perform_update(self, serializer):
        new_position = serializer.validated_data['position']
        playlist_song = serializer.instance
        old_position = playlist_song.position

        if new_position > old_position:
            PlaylistSong.objects.filter(
                playlist=playlist_song.playlist,
                position__gt=old_position,
                position__lte=new_position
            ).update(position=models.F('position') - 1)
            # return Response(data={'message': "Song has been moved to the new position in the playlist."}, status=status.HTTP_200_OK)

        else:
            PlaylistSong.objects.filter(
                playlist=playlist_song.playlist,
                position__lt=old_position,
                position__gte=new_position
            ).update(position=models.F('position') + 1)
            # return Response(data={'message': "Song has been moved to the new position in the playlist."}, status=status.HTTP_200_OK)

        playlist_song.position = new_position
        playlist_song.save()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response("Song has been moved to the new position in the playlist.")

    
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except PlaylistSong.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        playlist = instance.playlist
        position = instance.position

        # Update positions of other songs
        PlaylistSong.objects.filter(
            playlist=playlist,
            position__gt=position
        ).update(position=models.F('position') - 1)

        self.perform_destroy(instance)
        
        return Response("Song has been removed from the playlist.")


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



class PlaylistPagination(PageNumberPagination):
    page_size = 10

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistDetailSerializer
    pagination_class = PlaylistPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        playlist_songs = instance.playlistsong_set.all()
        page = self.paginate_queryset(playlist_songs)
        serializer = PlaylistSongSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(serializer.data)
        return Response("The name of the playlist has been edited.")

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("The playlist has been deleted.")
        # return Response(data={'message': "The playlist has been deleted"}, status=status.HTTP_200_OK)

