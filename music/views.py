from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def album_detail(request, album_id):
    print "album detail"
    album = get_object_or_404(Album, id=album_id)
    # album = Album.objects.get(id=album_id)
    # return HttpResponse("<h2>Details for album: " + str(album) + "</h2>")
    return render(request, 'music/album_detail.html', {'album': album})


def favorite(request, album_id):
    print "running favorite"
    print "POST: ", request.POST
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        print "selected song?: ", selected_song
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/album_detail.html', {
            'album': album,
            'error_message': "YOU SUCK!"
        })
    else:
        print "fav?", selected_song.is_favorite
        selected_song.toggle_favorite()
        print "fav?", selected_song.is_favorite
        selected_song.save()
    return render(request, 'music/album_detail.html', {'album': album})