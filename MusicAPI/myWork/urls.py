
from django.urls import path
from .views import (
    SongListCreateView,
    PlaylistListCreateView,
    PlaylistDetailView,
    PlaylistSongListView,
    PlaylistSongUpdateView,
    
)

urlpatterns = [
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlists/<int:playlist_id>/songs/', PlaylistSongListView.as_view(), name='playlistsong-list'),
    path('playlists/<int:playlist_id>/songs/<int:song_id>/', PlaylistSongUpdateView.as_view(), name='playlistsong-update'),
    # path('playlists/<int:pk>/songs/<int:song_id>/', PlaylistSongDeleteView.as_view(), name='playlistsong-delete')
]
# i have combined the functionality of last url into 5th url itself. ANd also delteed the respected view