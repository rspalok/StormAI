from sclib import SoundcloudAPI, Track, Playlist
import playsound

api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library


def soundcloud():
    track = api.resolve('https://soundcloud.com/dakshay-ahuja/she-dont-know-milind-gaba')

    assert type(track) is Track

    filename = 'basic.mp3'

    with open(filename, 'wb+') as fp:
        track.write_mp3_to(fp)

    playsound.playsound(filename)

    return
