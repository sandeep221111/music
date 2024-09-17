
from rest_framework import serializers
from .models import Playlist, PlaylistSong, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'artist', 'release_year']


class PlaylistSongSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='song.name')
    artist = serializers.ReadOnlyField(source='song.artist')
    release_year = serializers.ReadOnlyField(source='song.release_year')

    class Meta:
        model = PlaylistSong
        fields = ['id', 'name', 'artist', 'release_year', 'position']

class PlaylistSongSerializer2(serializers.ModelSerializer):
    # song = SongSerializer()
    # print(song)

    class Meta:
        model = PlaylistSong
        fields = ['position']



class PlaylistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name']

class PlaylistDetailSerializer(serializers.ModelSerializer):
    songs = PlaylistSongSerializer(source='playlistsong_set', many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']